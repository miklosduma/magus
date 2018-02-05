from tkinter import (StringVar, IntVar, OptionMenu, Button, ttk,
                     Checkbutton, VERTICAL, N, W)

from magus_kalkulator.sebzes import return_penalty
from magus_kalkulator.random_body import pick_sub_parts
from magus_kalkulator.validate import validate_integer, FieldValidationError
from magus_kalkulator.interface_elements import CharacterValueField, organize_rows_to_left

from magus_kalkulator.magus_constants import (HEAD, TORSO, RARM, LARM, RLEG, LLEG,
                             HEAD_LIST, TORSO_LIST, TORSO_LIST_BEHIND,
                             RARM_LIST, LARM_LIST, RLEG_LIST, LLEG_LIST,
                             THRUST, SLASH, BLUDGEON, BITE, CLAW)


DAMAGE_PAGE_COLUMN = 0

DAMAGE_BUTTON_TEXT = 'Start'
SELECT_CHARACTER = 'Megtamadott'
SELECT_WEAPON = 'Tamado fegyver'
DAMAGE_TEXT = 'Sebzes'
TULUTES_TEXT = 'Tulutes'
ATUTES_TEXT = 'Atutes'

NO_CHARACTER = 'Valassz karaktert!'

# Types of attacking weapons. Used when calculating the damage
WEAPON_TYPES = [THRUST, SLASH, BLUDGEON, BITE, CLAW]

ATUTES_VALUES = [0, 1, 2, 3, 4, 5]

KEY_TEXT_DICT = {
    'ep_loss': 'EP veszteseg',
    'fp_loss': 'FP veszteseg',
    'hit_target': 'Talalati hely',
    'penalty': 'Hatrany'
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


UNIQUE_HEAD_LIST = get_unique_body_parts(HEAD_LIST)
UNIQUE_TORSO_LIST = get_unique_body_parts(TORSO_LIST)
UNIQUE_TORSO_LIST_BEHIND = TORSO_LIST_BEHIND
UNIQUE_RARM_LIST = get_unique_body_parts(RARM_LIST)
UNIQUE_LARM_LIST = get_unique_body_parts(LARM_LIST)
UNIQUE_RLEG_LIST = get_unique_body_parts(RLEG_LIST)
UNIQUE_LLEG_LIST = get_unique_body_parts(LLEG_LIST)

BODY_LISTS_DICT = {
    HEAD: UNIQUE_HEAD_LIST,
    TORSO: UNIQUE_TORSO_LIST,
    RARM: UNIQUE_RARM_LIST,
    LARM: UNIQUE_LARM_LIST,
    RLEG: UNIQUE_RLEG_LIST,
    LLEG: UNIQUE_LLEG_LIST
}

BODY_LISTS_DICT_BEHIND = {
    HEAD: UNIQUE_HEAD_LIST,
    TORSO: UNIQUE_TORSO_LIST_BEHIND,
    RARM: UNIQUE_RARM_LIST,
    LARM: UNIQUE_LARM_LIST,
    RLEG: UNIQUE_RLEG_LIST,
    LLEG: UNIQUE_LLEG_LIST
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
    def __init__(self, master, width, orient=VERTICAL):
        ttk.PanedWindow.__init__(self, master, width=width, orient=orient)
        self.master = master
        self.karakterek = self.master.karakterek
        self.messages = self.master.messages

        self.choose_frame = ChooseCharacterFrame(self)
        self.weapon_frame = WeaponTypeFrame(self)
        self.damage_frame = DamageFrame(self)
        self.piercing_frame = PiercingFrame(self)
        self.body_parts_frame = ChooseBodyPartFrame(self)

        organize_rows_to_left([self.choose_frame, self.weapon_frame,
                               self.damage_frame, self.piercing_frame, self.body_parts_frame], 0)


class ChooseCharacterFrame(ttk.LabelFrame):
    def __init__(self, master):
        self.master = master
        ttk.LabelFrame.__init__(self, master, text=SELECT_CHARACTER)
        self.selected_character = KarakterVar(self, self.master.karakterek,
                                              self.master.messages)
        self.character_menu = KarakterekMenu(self, self.selected_character,
                                             self.master.karakterek, *[''])
        self.character_menu.grid()

    def get_selected(self):
        return self.selected_character.get_value()


class WeaponTypeFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=SELECT_WEAPON)
        self.selected_weapon = WeaponString(self, WEAPON_TYPES)
        self.weapon_menu = OptionMenu(self, self.selected_weapon,
                                      *WEAPON_TYPES)
        self.weapon_menu.grid()

    def get_weapon(self):
        return self.selected_weapon.get_weapon_type()


class DamageFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=DAMAGE_TEXT)
        self.damage = CharacterValueField(self, validate_integer)
        self.tulutes = TulutesBox(self)
        self.damage.grid(row=0, column=0)
        self.tulutes.grid(row=0, column=1)

    def get_damage(self):
        try:
            damage = self.damage.get_validated()
            return True, damage

        except FieldValidationError as error:
            return False, error.message

    def is_critical(self):
        return self.tulutes.get_tulutes()


class PiercingFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=ATUTES_TEXT)
        self.piercing_menu = AtutesMenu(self, *ATUTES_VALUES)
        self.piercing_menu.grid()

    def get_piercing(self):
        return self.piercing_menu.get_atutes()


class ChooseBodyPartFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text='Talalat helye')

        self.main_body_frame = ChooseMainBodyPartFrame(self)
        self.from_behind_box = FromBehind(self)
        self.from_behind_box.grid(row=0, column=0, sticky=(N, W))

        self.main_body_frame.grid(row=1, column=0)
        self.sub_body_frame = ChooseSubBodyPartFrame(self,
                                                     self.main_body_frame)
        self.sub_body_frame.grid(row=1, column=1)

    def get_targeted(self):
        main_part = self.main_body_frame.main_body_part.get()

        if main_part == 'Barhol':
            return '', ''

        sub_part = self.sub_body_frame.selected_sub_part

        if not sub_part:
            return main_part, ''

        return main_part, sub_part

    def is_from_behind(self):
        return self.from_behind_box.get_from_behind()


class FromBehind(Checkbutton):
    def __init__(self, master):
        self.main_body_frame = master.main_body_frame
        self.tick = IntVar()
        self.tick.set(0)
        self.state = self.tick.get()
        Checkbutton.__init__(self, master, text='Hatulrol',
                             variable=self.tick, command=self.print_on_change)

    def print_on_change(self, *_args):
        self.main_body_frame.main_body_part.set('Barhol')
        self.state = self.tick.get()

        if self.state:
            print('Selected')
        else:
            print('Unselected')

    def get_from_behind(self):
        return self.tick.get()


class ChooseMainBodyPartFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text='Fo testresz')
        self.main_body_part = StringVar()
        self.main_body_part.set('Barhol')
        self.main_body_parts = OptionMenu(self, self.main_body_part, *['Barhol',
                                                                       HEAD,
                                                                       TORSO,
                                                                       RARM,
                                                                       LARM,
                                                                       RLEG,
                                                                       LLEG])
        self.main_body_parts.grid()


class ChooseSubBodyPartFrame(ttk.LabelFrame):
    def __init__(self, master, main_body_frame):
        ttk.LabelFrame.__init__(self, master, text='Al testresz')
        self.master = master
        self.selected_sub_parts = None
        self.selected_sub_part = None
        self.main_body_frame = main_body_frame
        self.main_body_part = main_body_frame.main_body_part
        self.main_body_part.trace('w', self._follow_main_bodypart)
        self.sub_body_part = StringVar()
        self.sub_body_part.set('Barhol')
        self.sub_body_part.trace('w', self._follow_sub_part)
        self.sub_body_parts = OptionMenu(self, self.sub_body_part, *['Barhol'])
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

        if selected_sub_part and selected_sub_part != 'Barhol':
            self.selected_sub_part = [x for x in self.selected_sub_parts if selected_sub_part in x][0]
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
        if selected_main_body_part != 'Barhol':
            [_main_part, sub_parts] = body_list_map[selected_main_body_part]

            # Sub parts are a list of lists with two elements
            # E.g. [['Mellkas', 'sziv'],..]. Save choices to state
            self.selected_sub_parts = sub_parts
            print(self.selected_sub_parts)

            # Only use the second element of sub body part for options
            choices = ['Barhol'] + [x[1] for x in sub_parts]

        # If no main body part is selected, sub parts can only be Barhol.
        else:
            self.selected_sub_parts = None
            choices = ['Barhol']

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

        # Set dropdown to first element in list. ('Barhol')
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


class KarakterVar(StringVar):
    """
    Variable for selected character.
    """
    def __init__(self, master, karakterek, messages):
        """
        Initialise variable.
        """
        StringVar.__init__(self, master)
        self.set_value('')
        self.master = master
        self.karakterek = karakterek
        self.messages = messages
        self.trace('w', self.print_on_change)

    def set_value(self, value):
        """
        Set value to selected.
        """
        self.set(value)

    def get_value(self):
        """
        Return latest value.
        """
        character = self.get()

        if character:
            return True, character

        return False, NO_CHARACTER

    def print_on_change(self, *_args):
        """
        Print latest value and max_ep of
        selected character.
        """
        print(self.get())
        print(self.karakterek.get_karakter(
            self.get()).max_ep)
        self.messages.write_message(self.get())


class KarakterekMenu(OptionMenu):
    """
    Drop-down for character selection.
    """

    def __init__(self, master, variable, karakterek, *choices):
        """
        Initialise drop-down.
        """
        # Get already-added characters
        self.karakterek = karakterek
        OptionMenu.__init__(self, master, variable, *choices)
        self.variable = variable

        # Every time the drop-down is selected, update values for selection
        self.bind('<Button-1>', self._update)
        self.config(width=10)

    def _width_match_longest(self, list):

        if list:
            lengths = [len(x) for x in list]
            self.config(width=max(lengths) + 2)

    def _update(self, _event):
        """
        When clicking the drop-down, get the name of
        all characters currently in memory.
        """
        menu = self.children['menu']
        menu.delete(0, 'end')
        new_choices = self.karakterek.get_all_karakters()

        self._width_match_longest(new_choices)

        for value in new_choices:
            menu.add_command(label=value,
                             command=lambda v=value: self.variable.set(v))


class SebzesButton(Button):
    def __init__(self, master, text):
        Button.__init__(self, master, text=text)
        self.master = master
        self.karakterek = self.master.karakterek
        self.messages = self.master.messages
        self.main_panel = self.master.main_panel

        self.choose_frame = self.main_panel.choose_frame
        self.weapon_frame = self.main_panel.weapon_frame
        self.damage_frame = self.main_panel.damage_frame
        self.piercing_frame = self.main_panel.piercing_frame
        self.body_frame = self.main_panel.body_parts_frame

        self.bind('<Button-1>', self.write_results)

    def write_results(self, _event):

        is_from_behind = self.body_frame.is_from_behind()
        main_part, sub_parts = self.body_frame.get_targeted()
        key_word_args = {}

        if is_from_behind:
            key_word_args['from_behind'] = True

        if main_part:
            key_word_args['main_part'] = main_part

        if sub_parts:
            key_word_args['sub_part'] = sub_parts

        body_parts_list = pick_sub_parts(**key_word_args)

        attacking_weapon = self.weapon_frame.get_weapon()
        success, attacked = self.choose_frame.get_selected()

        if not success:
            self.messages.write_message(attacked)
            return

        max_ep = self.karakterek.get_karakter(attacked).max_ep
        sfe = self.karakterek.get_karakter(attacked).sfe

        success, result = self.damage_frame.get_damage()

        if not success:
            self.messages.write_message(result)
            return

        damage = result

        tulutes = self.damage_frame.is_critical()
        atutes = self.piercing_frame.get_piercing()

        penalty = return_penalty(sfe, damage, body_parts_list, max_ep, attacking_weapon,
                                 tulutes=tulutes, atutes=atutes)
        msg = format_damage_msg(penalty)
        self.messages.write_message(msg)


class TulutesBox(Checkbutton):
    def __init__(self, master):
        self.tick = IntVar()
        self.tick.set(0)
        self.state = self.tick.get()
        Checkbutton.__init__(self, master, text=TULUTES_TEXT,
                             variable=self.tick, command=self.print_on_change)

    def print_on_change(self, *_args):
        self.state = self.tick.get()

        if self.state:
            print('Selected')
        else:
            print('Unselected')

    def get_tulutes(self):
        return self.tick.get()


class AtutesMenu(OptionMenu):
    def __init__(self, master, *options):
        self.atutes = IntVar()
        self.atutes.trace('w', callback=self.print_on_change)
        self.atutes.set(options[0])
        OptionMenu.__init__(self, master, self.atutes, *options)

    def print_on_change(self, *_args):
        print(self.get_atutes())

    def get_atutes(self):
        return self.atutes.get()
