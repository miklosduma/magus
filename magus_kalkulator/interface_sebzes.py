"""
Classes used by Damage page.
"""

from tkinter import StringVar, IntVar, ttk, VERTICAL, N, W

from magus_kalkulator.sebzes import return_penalty
from magus_kalkulator.random_body import pick_sub_parts
from magus_kalkulator.validate import validate_integer, FieldValidationError
from magus_kalkulator.interface_elements import (CharacterValueField,
                                                 organize_rows_to_left,
                                                 ChooseCharacterFrame,
                                                 on_all_children,
                                                 CharacterDropDown,
                                                 format_list_msg, Spinbox)

from magus_kalkulator import magus_constants as mgc

DAMAGE_PAGE_COLUMN = 0

DAMAGE_BUTTON_TEXT = 'Start'
SELECT_CHARACTER = 'Megtamadott'
SELECT_WEAPON = 'Tamado fegyver'
DAMAGE_TEXT = 'Sebzes'
TULUTES_TEXT = 'Tulutes'
ATUTES_TEXT = 'Atutes'
HIT_LABEL = 'Talalat helye'
FROM_BACK_LABEL = 'Hatulrol'
ANYWHERE = 'Barhol'
MAIN_PART_LABEL = 'Fo testresz'
SUB_PART_LABEL = 'Al testresz'

# Types of attacking weapons. Used when calculating the damage
WEAPON_TYPES = (mgc.THRUST, mgc.SLASH, mgc.BLUDGEON, mgc.BITE, mgc.CLAW)

ATUTES_VALUES = [0, 1, 2, 3, 4, 5]

EP_LOSS_KEY = 'ep_loss'
FP_LOSS_KEY = 'fp_loss'
HIT_KEY = 'hit_target'
PENALTY_KEY = 'penalty'

KEY_TEXT_DICT = {
    EP_LOSS_KEY: 'EP veszteseg',
    FP_LOSS_KEY: 'FP veszteseg',
    HIT_KEY: 'Talalati hely',
    PENALTY_KEY: 'Hatrany'
}


def remove_duplicates(a_list):
    """
    Removes all duplicates from a list, making sure
    each elem is unique.
    """
    for elem in a_list:
        while a_list.count(elem) > 1:
            a_list.remove(elem)

    return a_list


def get_unique_body_parts(body_parts_list):
    """
    Used in removing duplicates from a body parts
    list.
    """
    [main_part, sub_parts_list] = body_parts_list
    unique_sub_parts_list = remove_duplicates(sub_parts_list)
    return [main_part, unique_sub_parts_list]


UNIQUE_HEAD_LIST = get_unique_body_parts(mgc.HEAD_LIST)
UNIQUE_TORSO_LIST = get_unique_body_parts(mgc.TORSO_LIST)
UNIQUE_TORSO_LIST_BEHIND = mgc.TORSO_LIST_BEHIND
UNIQUE_RARM_LIST = get_unique_body_parts(mgc.RARM_LIST)
UNIQUE_LARM_LIST = get_unique_body_parts(mgc.LARM_LIST)
UNIQUE_RLEG_LIST = get_unique_body_parts(mgc.RLEG_LIST)
UNIQUE_LLEG_LIST = get_unique_body_parts(mgc.LLEG_LIST)

BODY_LISTS_DICT = {
    mgc.HEAD: UNIQUE_HEAD_LIST,
    mgc.TORSO: UNIQUE_TORSO_LIST,
    mgc.RARM: UNIQUE_RARM_LIST,
    mgc.LARM: UNIQUE_LARM_LIST,
    mgc.RLEG: UNIQUE_RLEG_LIST,
    mgc.LLEG: UNIQUE_LLEG_LIST
}

BODY_LISTS_DICT_BEHIND = {
    mgc.HEAD: UNIQUE_HEAD_LIST,
    mgc.TORSO: UNIQUE_TORSO_LIST_BEHIND,
    mgc.RARM: UNIQUE_RARM_LIST,
    mgc.LARM: UNIQUE_LARM_LIST,
    mgc.RLEG: UNIQUE_RLEG_LIST,
    mgc.LLEG: UNIQUE_LLEG_LIST
}


def format_damage_msg(penalty_dict):
    """
    Formats message returned on
    penalty calculation.
    """
    msg = ''

    for key, value in sorted(penalty_dict.items()):

        # Replace actual key with key text.
        key = KEY_TEXT_DICT[key]

        if isinstance(value, list):
            value = format_list_msg(value)

        msg += '{}: {}\n'.format(key, value)

    return msg.strip()


class SebzesPage(ttk.Frame):
    """
    Main tab for calculating damage and penalties.
    """
    def __init__(self, master_tabs, characters, messages):
        """
        Initializes damage tab.
        """
        ttk.Frame.__init__(self, master_tabs)
        self.panel = CharacterPanel(self, characters, messages,
                                    orient=VERTICAL)
        self.panel.grid()

    def reset_page(self):
        self.panel.reset_panel()


class CharacterPanel(ttk.PanedWindow):
    """
    Main panel of damage page.
    """
    def __init__(self, page, characters, messages, **kwargs):
        """
        Initialise main panel.
        """
        ttk.PanedWindow.__init__(self, page, **kwargs)
        self.messages = messages
        self.characters = characters

        sebzes_button = ttk.Button(self, text=DAMAGE_BUTTON_TEXT)
        sebzes_button.bind('<Button-1>', self.write_results)
        self.zero_zero_state = IntVar()
        self.zero_zero_state.trace('w', self.set_piercing_state)

        self.choose_frame = ChooseCharacterFrame(self, characters)
        self.weapon_frame = WeaponTypeFrame(self)
        self.piercing_frame = PiercingFrame(self, ATUTES_VALUES)
        self.damage_frame = DamageFrame(self, self.zero_zero_state)
        self.body_parts_frame = ChooseBodyPartFrame(self)

        last_row = organize_rows_to_left([self.choose_frame, self.weapon_frame,
                                          self.damage_frame, self.piercing_frame,
                                          self.body_parts_frame], 0)
        sebzes_button.grid(row=last_row, padx=8, pady=4, sticky=W)

    def set_piercing_state(self, *_event):
        if self.zero_zero_state.get():
            self.piercing_frame.piercing_menu.disable()

        else:
            self.piercing_frame.piercing_menu.enable()

    def reset_panel(self):
        """
        Resets all child widgets of the panel.
        """
        on_all_children('reset_frame', self)

    def write_results(self, _event):
        """
        Gets result based on input fields/values and writes
        result to message panel.
        """
        success, attacked = self.choose_frame.get_selected()

        if not success:
            self.messages.write_message(attacked)
            return

        character = self.characters.get_character(attacked)

        success, damage = self.damage_frame.get_damage()

        if not success:
            self.messages.write_message(damage)
            return

        attacking_weapon = self.weapon_frame.get_weapon()
        body_parts_list = self.body_parts_frame.get_targeted()

        kwargs = dict()

        kwargs['tulutes'] = self.damage_frame.is_critical()

        is_zero_zero = self.damage_frame.is_zero_zero()

        if is_zero_zero:
            kwargs['is_zero_zero'] = is_zero_zero

        else:
            kwargs['atutes'] = self.piercing_frame.get_piercing()

        result = return_penalty(character, damage, body_parts_list,
                                attacking_weapon, **kwargs)

        self.messages.delete_message()
        self.messages.write_damage(result)
        self.reset_panel()


class WeaponTypeFrame(ttk.LabelFrame):
    """
    Frame for weapon-type selection drop-down.
    """
    def __init__(self, character_panel):
        """
        Initialises weapon-type frame.
        """
        ttk.LabelFrame.__init__(self, character_panel, text=SELECT_WEAPON)
        self.weapon_menu = CharacterDropDown(self, values=WEAPON_TYPES)
        self.reset_frame()
        self.weapon_menu.grid()

    def get_weapon(self):
        """
        Returns selected weapon.
        """
        return self.weapon_menu.get()

    def reset_frame(self):
        """
        Resets all child widgets of the frame.
        """
        self.weapon_menu.reset_drop_down()


class DamageFrame(ttk.LabelFrame):
    """
    Frame comprising damage entry field.
    """
    def __init__(self, character_panel, zero_zero_var):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, character_panel, text=DAMAGE_TEXT)
        self.damage = CharacterValueField(self, validate_integer)

        self.critical_state = IntVar()
        self.critical_state.set(0)
        self.tulutes = ttk.Checkbutton(self, text=TULUTES_TEXT,
                                       variable=self.critical_state)

        self.zero_zero_state = zero_zero_var
        self.zero_zero_state.set(0)
        self.zero_zero = ttk.Checkbutton(self, text='00',
                                         variable=self.zero_zero_state)

        self.damage.grid(row=0, column=0)
        self.tulutes.grid(row=0, column=1)
        self.zero_zero.grid(row=0, column=2)

    def reset_frame(self):
        """
        Resets all child widgets of the frame.
        """
        self.damage.reset_fld()
        self.critical_state.set(0)
        self.zero_zero_state.set(0)

    def get_damage(self):
        """
        Tries to return value of entry field. Returns
        an error message if the value of the field
        is invalid.
        """
        try:
            damage = self.damage.get_validated()
            return True, damage

        except FieldValidationError as error:
            return False, error.message

    def is_critical(self):
        """
        Checks whether the critical tick-box is checked.
        """
        return self.critical_state.get()

    def is_zero_zero(self):
        """
        Checks whether the 00 tickbox is checked.
        """
        return self.zero_zero_state.get()


class PiercingFrame(ttk.LabelFrame):
    """
    Frame comprising the armour-piercing value drop-down.
    """
    def __init__(self, character_panel, piercing_values):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, character_panel, text=ATUTES_TEXT)

        self.piercing_menu = Spinbox(self, from_=0, to=5)
        self.reset_frame()
        self.piercing_menu.grid()

    def get_piercing(self):
        """
        Retrieves value of AP drop-down.
        """
        return int(self.piercing_menu.get())

    def reset_frame(self):
        """
        Resets the piercing value to 0.
        """
        self.piercing_menu.set(0)


class ChooseBodyPartFrame(ttk.LabelFrame):
    """
    Master frame for body selection drop-downs.
    """
    def __init__(self, character_panel):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, character_panel, text=HIT_LABEL)

        self.main_body_frame = ChooseMainBodyPartFrame(self)
        self.behind_state = IntVar()
        self.behind_state.set(0)
        self.from_behind_box = ttk.Checkbutton(self, text=FROM_BACK_LABEL,
                                               variable=self.behind_state,
                                               command=self.set_state)

        self.from_behind_box.grid(row=0, column=0, sticky=(N, W))

        self.main_body_frame.grid(row=1, column=0)
        self.sub_body_frame = ChooseSubBodyPartFrame(self,
                                                     self.main_body_frame)
        self.sub_body_frame.grid(row=1, column=1)

    def get_parts(self):
        """
        Retrieves the selected main and sub-body parts, if any.
        """
        main_part = self.main_body_frame.main_body_part.get()

        if main_part == ANYWHERE:
            return None, None

        sub_part = self.sub_body_frame.selected_sub_part

        if not sub_part:
            return main_part, None

        return main_part, sub_part

    def set_state(self, *_args):
        """
        Set the state based on tick-box being selected or not.
        Also, reset main body part drop-down as any selected value
        can become invalid once the attack comes from behind not from
        the front or vice versa.
        """
        self.main_body_frame.reset_frame()

    def is_from_behind(self):
        """
        Gets the state of the from-behind tick-box.
        """
        return self.behind_state.get()

    def get_targeted(self):
        """
        Either returns the selected body parts - if any -
        or selects a random set of body parts.

        Also takes into account whether the attack happens
        from behind.
        """
        is_from_behind = self.is_from_behind()
        main_part, sub_part = self.get_parts()

        return pick_sub_parts(from_behind=is_from_behind,
                              main_part=main_part,
                              sub_part=sub_part)

    def reset_frame(self):
        """
        Resets the child widgets of the element and
        also sets the from behind checkbox to False.
        """
        self.behind_state.set(0)
        on_all_children('reset_frame', self)


class ChooseMainBodyPartFrame(ttk.LabelFrame):
    """
    Main body-part drop-down frame.
    """
    def __init__(self, body_frame):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, body_frame, text=MAIN_PART_LABEL)
        self.main_body_part = StringVar()
        self.main_body_parts = CharacterDropDown(self, textvariable=self.main_body_part,
                                                 values=[ANYWHERE, mgc.HEAD, mgc.TORSO,
                                                         mgc.RARM, mgc.LARM, mgc.RLEG,
                                                         mgc.LLEG])
        self.main_body_parts.bind()

        self.main_body_parts.grid()
        self.reset_frame()

    def reset_frame(self):
        """
        Sets the main body part selection drop-down to
        anywhere, triggering the same change in the sub drop-down too.
        """
        self.main_body_parts.set(ANYWHERE)


class ChooseSubBodyPartFrame(ttk.LabelFrame):
    """
    Sub body-part frame.
    """
    def __init__(self, body_frame, main_body_frame):
        """
        Initialise sub body part frame.
        """
        ttk.LabelFrame.__init__(self, body_frame, text=SUB_PART_LABEL)
        self.body_frame = body_frame
        self.selected_sub_parts = None
        self.selected_sub_part = None
        self.main_body_frame = main_body_frame
        self.main_body_part = main_body_frame.main_body_part
        self.main_body_part.trace('w', self._follow_main_bodypart)
        self.sub_body_part = StringVar()
        self.sub_body_part.set(ANYWHERE)
        self.sub_body_part.trace('w', self._follow_sub_part)
        self.sub_body_parts = CharacterDropDown(self,
                                                textvariable=self.sub_body_part,
                                                values=[ANYWHERE])
        self.sub_body_parts.grid()

    def _follow_sub_part(self, *_args):
        """
        Traces the sub body part selected. Since the
        damage calculation expects the sub body part to
        be a list of two, this function selects the
        corresponding pair based on the selected sub part.

        E.g. if Breastbone is selected, the pair will be
        [Chest, Breastbone].
        """
        selected_sub_part = self.sub_body_part.get()

        if selected_sub_part and selected_sub_part != ANYWHERE:
            self.selected_sub_part = [x for x in self.selected_sub_parts
                                      if selected_sub_part in x][0]
        else:
            self.selected_sub_part = None

    def _follow_main_bodypart(self, *_args):
        """
        Sub body parts dropdown follows changes in
        the main body part dropwdown.
        """
        # Get currently selected value of main dropdown.
        selected_main_body_part = self.main_body_part.get()

        # See if from behind box is ticked
        is_from_behind = self.body_frame.is_from_behind()

        if is_from_behind:
            body_list_map = BODY_LISTS_DICT_BEHIND
        else:
            body_list_map = BODY_LISTS_DICT

        # Calculate options for sub part dropdown if a main part is selected.
        if selected_main_body_part != ANYWHERE:

            # Sub parts are a list of lists with two elements
            # E.g. [['Mellkas', 'sziv'],..]. Save choices to state
            self.selected_sub_parts = body_list_map[selected_main_body_part][1]

            # Only use the second element of sub body part for options
            choices = [ANYWHERE] + [x[1] for x in self.selected_sub_parts]

        # If no main body part is selected, sub parts can only be ANYWHERE.
        else:
            self.selected_sub_parts = None
            choices = [ANYWHERE]

        # Update drop-down menu with choices.
        self._update(choices)

    def _update(self, list_of_choices):
        """
        Update dropdown with supported choices.
        """
        if list_of_choices:
            self.sub_body_parts['values'] = list_of_choices

            # Set dropdown to first element in list. (ANYWHERE)
            self.sub_body_part.set(list_of_choices[0])

            # Calculate width based on longest list element.
            self.sub_body_parts.width_match_longest(list_of_choices)
