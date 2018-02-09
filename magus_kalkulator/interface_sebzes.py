"""
Classes used by Damage page.
"""

from tkinter import (StringVar, IntVar, OptionMenu, Button, ttk,
                     Checkbutton, VERTICAL, N, W)

from magus_kalkulator.sebzes import return_penalty
from magus_kalkulator.random_body import pick_sub_parts
from magus_kalkulator.validate import validate_integer, FieldValidationError
from magus_kalkulator.interface_elements import (CharacterValueField,
                                                 organize_rows_to_left)

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

NO_CHARACTER = 'Valassz karaktert!'

# Types of attacking weapons. Used when calculating the damage
WEAPON_TYPES = [mgc.THRUST, mgc.SLASH, mgc.BLUDGEON, mgc.BITE, mgc.CLAW]

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

        if isinstance(value, list):
            value = ', '.join(value)

        msg += '{}: {}\n'.format(KEY_TEXT_DICT[key], value)

    return msg.strip()


class SebzesPage(ttk.Frame):
    """
    Main tab for calculating damage and penalties.
    """
    def __init__(self, master, master_gui, width):
        """
        Initializes damage tab.
        """
        ttk.Frame.__init__(self, master, width=width)
        self.messages = master_gui.messages

        # Variable for character selection drop-down
        # SFE and Max_EP of character is used when calculating damage
        self.karakterek = master_gui.karakterek
        self.main_panel = CharacterPanel(self, width)
        self.sebzes_button = SebzesButton(self, DAMAGE_BUTTON_TEXT)

        # Place elements on grid
        organize_rows_to_left([self.main_panel,
                               self.sebzes_button], DAMAGE_PAGE_COLUMN)


class CharacterPanel(ttk.PanedWindow):
    """
    Main panel of damage page.
    """
    def __init__(self, master, width, orient=VERTICAL):
        """
        Initialise main panel.
        """
        ttk.PanedWindow.__init__(self, master, width=width, orient=orient)
        self.master = master

        self.choose_frame = ChooseCharacterFrame(self, self.master.karakterek)
        self.weapon_frame = WeaponTypeFrame(self)
        self.damage_frame = DamageFrame(self)
        self.piercing_frame = PiercingFrame(self)
        self.body_parts_frame = ChooseBodyPartFrame(self)

        organize_rows_to_left([self.choose_frame, self.weapon_frame,
                               self.damage_frame, self.piercing_frame,
                               self.body_parts_frame], 0)


class ChooseCharacterFrame(ttk.LabelFrame):
    """
    Frame comprising character-selection drop-down.
    """
    def __init__(self, master, karakterek):
        """
        Initialise character-selection frame.
        """
        self.master = master
        ttk.LabelFrame.__init__(self, master, text=SELECT_CHARACTER)
        self.karakterek = karakterek
        self.variable = StringVar()
        self.variable.set('')
        self.character_menu = OptionMenu(self, self.variable, *[''])
        self.character_menu.bind('<Button-1>', self._update)
        self.character_menu.config(width=10)
        self.character_menu.grid()

    def get_selected(self):
        """
        Return latest value.
        """
        character = self.variable.get()

        if character:
            return True, character

        return False, NO_CHARACTER

    def _width_match_longest(self, opt_list):
        """
        Width of menu list must match longest menu item.
        """

        if opt_list:
            lengths = [len(x) for x in opt_list]
            self.character_menu.config(width=max(lengths) + 2)

    def _update(self, _event):
        """
        When clicking the drop-down, get the name of
        all characters currently in memory.
        """
        menu = self.character_menu.children['menu']
        menu.delete(0, 'end')
        new_choices = self.karakterek.get_all_karakters()

        self._width_match_longest(new_choices)

        for value in new_choices:
            menu.add_command(label=value,
                             command=lambda v=value: self.variable.set(v))


class WeaponTypeFrame(ttk.LabelFrame):
    """
    Frame for weapon-type selection drop-down.
    """
    def __init__(self, master):
        """
        Initialises weapon-type frame.
        """
        ttk.LabelFrame.__init__(self, master, text=SELECT_WEAPON)
        self.selected_weapon = WeaponString(self, WEAPON_TYPES)
        self.weapon_menu = OptionMenu(self, self.selected_weapon,
                                      *WEAPON_TYPES)
        self.weapon_menu.grid()

    def get_weapon(self):
        """
        Returns selected weapon.
        """
        return self.selected_weapon.get_weapon_type()


class DamageFrame(ttk.LabelFrame):
    """
    Frame comprising damage entry field.
    """
    def __init__(self, master):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, master, text=DAMAGE_TEXT)
        self.damage = CharacterValueField(self, validate_integer)
        self.critical_state = IntVar()
        self.critical_state.set(0)
        self.tulutes = Checkbutton(self, text=TULUTES_TEXT,
                                   variable=self.critical_state)
        self.damage.grid(row=0, column=0)
        self.tulutes.grid(row=0, column=1)

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


class PiercingFrame(ttk.LabelFrame):
    """
    Frame comprising the armour-piercing value drop-down.
    """
    def __init__(self, master):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, master, text=ATUTES_TEXT)
        self.piercing_menu = AtutesMenu(self, *ATUTES_VALUES)
        self.piercing_menu.grid()

    def get_piercing(self):
        """
        Retrieves value of AP drop-down.
        """
        return self.piercing_menu.get_atutes()


class ChooseBodyPartFrame(ttk.LabelFrame):
    """
    Master frame for body selection drop-downs.
    """
    def __init__(self, master):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, master, text=HIT_LABEL)

        self.main_body_frame = ChooseMainBodyPartFrame(self)
        self.behind_state = IntVar()
        self.behind_state.set(0)
        self.from_behind_box = Checkbutton(self, text=FROM_BACK_LABEL,
                                           variable=self.behind_state,
                                           command=self.set_state)

        self.from_behind_box.grid(row=0, column=0, sticky=(N, W))

        self.main_body_frame.grid(row=1, column=0)
        self.sub_body_frame = ChooseSubBodyPartFrame(self,
                                                     self.main_body_frame)
        self.sub_body_frame.grid(row=1, column=1)

    def get_targeted(self):
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
        self.main_body_frame.main_body_part.set(ANYWHERE)

    def is_from_behind(self):
        """
        Gets the state of the from-behind tick-box.
        """
        return self.behind_state.get()


class ChooseMainBodyPartFrame(ttk.LabelFrame):
    """
    Main body-part drop-down frame.
    """
    def __init__(self, master):
        """
        Initialises frame.
        """
        ttk.LabelFrame.__init__(self, master, text=MAIN_PART_LABEL)
        self.main_body_part = StringVar()
        self.main_body_part.set(ANYWHERE)
        self.main_body_parts = OptionMenu(self,
                                          self.main_body_part,
                                          *[ANYWHERE, mgc.HEAD, mgc.TORSO,
                                            mgc.RARM, mgc.LARM, mgc.RLEG,
                                            mgc.LLEG])
        self.main_body_parts.grid()


class ChooseSubBodyPartFrame(ttk.LabelFrame):
    """
    Sub body-part frame.
    """
    def __init__(self, master, main_body_frame):
        """
        Initialise sub body part frame.
        """
        ttk.LabelFrame.__init__(self, master, text=SUB_PART_LABEL)
        self.master = master
        self.selected_sub_parts = None
        self.selected_sub_part = None
        self.main_body_frame = main_body_frame
        self.main_body_part = main_body_frame.main_body_part
        self.main_body_part.trace('w', self._follow_main_bodypart)
        self.sub_body_part = StringVar()
        self.sub_body_part.set(ANYWHERE)
        self.sub_body_part.trace('w', self._follow_sub_part)
        self.sub_body_parts = OptionMenu(self,
                                         self.sub_body_part,
                                         *[ANYWHERE])
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
        is_from_behind = self.master.is_from_behind()

        if is_from_behind:
            body_list_map = BODY_LISTS_DICT_BEHIND
        else:
            body_list_map = BODY_LISTS_DICT

        # Calculate options for sub part dropdown if a main part is selected.
        if selected_main_body_part != ANYWHERE:
            [_main_part, sub_parts] = body_list_map[selected_main_body_part]

            # Sub parts are a list of lists with two elements
            # E.g. [['Mellkas', 'sziv'],..]. Save choices to state
            self.selected_sub_parts = sub_parts
            print(self.selected_sub_parts)

            # Only use the second element of sub body part for options
            choices = [ANYWHERE] + [x[1] for x in sub_parts]

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
        menu = self.sub_body_parts.children['menu']
        menu.delete(0, 'end')

        for value in list_of_choices:
            menu.add_command(label=value,
                             command=lambda v=value: self.sub_body_part.set(v))

        # Set dropdown to first element in list. (ANYWHERE)
        self.sub_body_part.set(list_of_choices[0])


class WeaponString(StringVar):
    """
    Variable for attacking weapon.
    """
    def __init__(self, master, weapon_types):
        """
        Initialise variable for attacking
        weapon.
        """
        StringVar.__init__(self, master)
        self.weapon_types = weapon_types
        self.initial = weapon_types[0]
        self.set_weapon_type(self.initial)
        self.trace('w', self.print_on_change)

    def set_weapon_type(self, value):
        """
        Sets value of variable to latest selected
        value.
        """
        self.set(value)

    def get_weapon_type(self):
        """
        Returns currently selected weapon.
        """
        return self.get()

    def print_on_change(self, *_args):
        """
        Prints value on changes.
        """
        print(self.get_weapon_type())


class SebzesButton(Button):
    """
    Damage button.
    """
    def __init__(self, master, text):
        """
        Initialise button.
        """
        Button.__init__(self, master, text=text)
        self.master = master
        self.karakterek = self.master.karakterek
        self.messages = self.master.messages
        self.main_panel = self.master.main_panel
        self.bind('<Button-1>', self.write_results)

    def write_results(self, _event):
        """
        Gets result based on input fields/values and writes
        result to message panel.
        """
        is_from_behind = self.main_panel.body_parts_frame.is_from_behind()
        main_part, sub_parts = self.main_panel.body_parts_frame.get_targeted()

        body_parts_list = pick_sub_parts(from_behind=is_from_behind,
                                         main_part=main_part,
                                         sub_part=sub_parts)

        attacking_weapon = self.main_panel.weapon_frame.get_weapon()
        success, attacked = self.main_panel.choose_frame.get_selected()

        if not success:
            self.messages.write_message(attacked)
            return

        character = self.karakterek.get_karakter(attacked)

        success, result = self.main_panel.damage_frame.get_damage()

        if not success:
            self.messages.write_message(result)
            return

        tulutes = self.main_panel.damage_frame.is_critical()
        atutes = self.main_panel.piercing_frame.get_piercing()

        penalty = return_penalty(character.sfe, result, body_parts_list,
                                 character.max_ep, attacking_weapon,
                                 tulutes=tulutes, atutes=atutes)
        msg = format_damage_msg(penalty)
        self.messages.write_message(msg)





class AtutesMenu(OptionMenu):
    """
    Armour piercing menu.
    """
    def __init__(self, master, *options):
        """
        Init menu.
        """
        self.atutes = IntVar()
        self.atutes.set(options[0])
        OptionMenu.__init__(self, master, self.atutes, *options)

    def get_atutes(self):
        """
        Retrieve current value of AP drop-down.
        """
        return self.atutes.get()
