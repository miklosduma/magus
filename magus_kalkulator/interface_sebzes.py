from tkinter import (Entry, StringVar, IntVar ,OptionMenu, Button, ttk,
                     Label, Checkbutton)
from sebzes import return_penalty
from validate import validate_integer, FieldValidationError
from interface_elements import CharacterValueField, organize_rows_to_left


DAMAGE_PAGE_COLUMN = 0

DAMAGE_BUTTON_TEXT = 'Start'
SELECT_CHARACTER = 'Megtamadott'
SELECT_WEAPON = 'Tamado fegyver'
DAMAGE_TEXT = 'Sebzes'
TULUTES_TEXT = 'Tulutes'
ATUTES_TEXT = 'Atutes'

NO_CHARACTER = 'Valassz karaktert!'

# Types of attacking weapons. Used when calculating the damage
WEAPON_TYPES = ['Szur', 'Vag', 'Zuz', 'Harap', 'Karmol']

ATUTES_VALUES = [0, 1, 2, 3, 4, 5]

KEY_TEXT_DICT = {
    'ep_loss': 'EP veszteseg',
    'fp_loss': 'FP veszteseg',
    'hit_target': 'Talalati hely',
    'penalty': 'Hatrany'
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
        self.karakter_var = KarakterVar(self, self.karakterek, self.messages)

        self.karakter_label = Label(self, text=SELECT_CHARACTER)
        self.dropdown = KarakterekMenu(self, self.karakter_var,
                                       self.karakterek, *[''])

        # Variable for type of attacking weapon. Can be selected from drop-down
        self.weapon_label = Label(self, text=SELECT_WEAPON)
        self.weapon_type = WeaponString(self, WEAPON_TYPES)
        self.weapon_menu = WeaponTypeMenu(self, self.weapon_type, *WEAPON_TYPES)

        # Variable for total damage. Can be entered into entry field
        self.sebzes_label = Label(self, text=DAMAGE_TEXT)
        self.sebzes = CharacterValueField(self, validate_integer)
        self.tulutes_box = TulutesBox(self)
        self.atutes_label = Label(self, text=ATUTES_TEXT)
        self.atutes_menu = AtutesMenu(self, *ATUTES_VALUES)
        self.sebzes_button = SebzesButton(self, DAMAGE_BUTTON_TEXT)

        # Place elements on grid
        organize_rows_to_left([self.karakter_label, self.dropdown,
                                            self.weapon_label, self.weapon_menu,
                                            self.sebzes_label, self.sebzes,
                                            self.atutes_label, self.atutes_menu,
                                            self.sebzes_button], DAMAGE_PAGE_COLUMN)
        self.sebzes_row = self.sebzes.grid_info()['row']
        self.tulutes_box.grid(column=DAMAGE_PAGE_COLUMN+1, row=self.sebzes_row)


class WeaponTypeMenu(OptionMenu):
    """
    Drop-down for attacking weapon selection.
    """

    def __init__(self, master, variable, *weapon_types):
        """
        Initialise weapon drop-down.
        """
        OptionMenu.__init__(self, master, variable, *weapon_types)


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

    def print_on_change(self, *args):
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

    def print_on_change(self, *args):
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

    def _update(self, event):
        """
        When clicking the drop-down, get the name of
        all characters currently in memory.
        """
        menu = self.children['menu']
        menu.delete(0, 'end')
        new_choices = self.karakterek.get_all_karakters()
        for value in new_choices:
            menu.add_command(label=value,
                             command=lambda v=value: self.variable.set(v))


class SebzesButton(Button):
    def __init__(self, master, text):
        Button.__init__(self, master, text=text)
        self.master = master
        self.karakterek = self.master.karakterek
        self.karakter_var = self.master.karakter_var
        self.messages = self.master.messages
        self.tulutes = self.master.tulutes_box
        self.atutes = self.master.atutes_menu
        self.sebzes = self.master.sebzes
        self.weapon_type = self.master.weapon_type
        self.bind('<Button-1>', self.write_results)

    def get_damage(self):
        try:
            damage = self.sebzes.validate()
            return damage

        except FieldValidationError:
            raise

    def write_results(self, event):
        attacking_weapon = self.weapon_type.get()
        success, attacked = self.karakter_var.get_value()

        if not success:
            self.messages.write_message(attacked)
            return

        max_ep = self.karakterek.get_karakter(attacked).max_ep
        sfe = self.karakterek.get_karakter(attacked).sfe

        try:
            damage = self.get_damage()
        except FieldValidationError as error:
            self.messages.write_message(error.message)
            return

        tulutes = self.tulutes.get_tulutes()
        atutes = self.atutes.get_atutes()

        penalty = return_penalty(sfe, damage, atutes, max_ep, attacking_weapon,
                                 tulutes=tulutes)
        msg = format_damage_msg(penalty)
        self.messages.write_message(msg)


class TulutesBox(Checkbutton):
    def __init__(self, master):
        self.tick = IntVar()
        self.tick.set(0)
        Checkbutton.__init__(self, master, text=TULUTES_TEXT,
                             variable=self.tick, command=self.print_on_change)

    def print_on_change(self, *args):
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

    def print_on_change(self, *args):
        print(self.get_atutes())

    def get_atutes(self):
        return self.atutes.get()