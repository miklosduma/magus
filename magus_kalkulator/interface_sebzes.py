from tkinter import (Entry, StringVar, OptionMenu, Button, ttk)
from sebzes import return_penalty
from validate import validate_values


# Types of attacking weapons. Used when calculating the damage
WEAPON_TYPES = ['Szur', 'Vag', 'Zuz', 'Harap', 'Karmol']

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
    def __init__(self, master, master_gui):
        """
        Initializes damage tab.
        """
        ttk.Frame.__init__(self, master)
        self.messages = master_gui.messages

        # Variable for character selection drop-down
        # SFE and Max_EP of character is used when calculating damage
        self.karakterek = master_gui.karakterek
        self.karakter_var = KarakterVar(self, self.karakterek, self.messages)
        self.dropdown = KarakterekMenu(self, self.karakter_var,
                                       self.karakterek, *[''])

        # Variable for type of attacking weapon. Can be selected from drop-down
        self.weapon_type = WeaponString(self, WEAPON_TYPES)
        self.weapon_menu = WeaponTypeMenu(self, self.weapon_type, *WEAPON_TYPES)

        # Variable for total damage. Can be entered into entry field
        self.sebzes = SebzesField(self)
        self.sebzes_button = SebzesButton(self, 'Start')

        self.sebzes.grid(row=6, column=1)
        self.sebzes_button.grid(row=7, column=1)
        self.weapon_menu.grid(row=4, column=1)
        self.dropdown.grid(row=2, column=1)
        self.messages.grid(column=0, columnspan=4)


class SebzesField(Entry):
    """
    Input field for damage.
    """
    def __init__(self, master):
        """
        Initialise input field.
        """
        # Varible for entered damage
        self.sebzes = StringVar(master)
        self.sebzes.set('')
        self.sebzes.trace('w', self.print_on_change)

        # Entry field
        Entry.__init__(self, master, textvariable=self.sebzes)

    def get_sebzes(self):
        """
        Returns latest value of
        entry field.
        """
        return self.sebzes.get()

    def print_on_change(self, *args):
        """
        Prints changes to value of
        input field.
        """
        print(self.get_sebzes())


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

        return False, 'Valassz karaktert!'

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
        self.sebzes = self.master.sebzes
        self.weapon_type = self.master.weapon_type
        self.bind('<Button-1>', self.write_results)

    def get_damage(self):
        return self.sebzes.get()

    def write_results(self, event):
        attacking_weapon = self.weapon_type.get()
        success, attacked = self.karakter_var.get_value()

        if not success:
            self.messages.write_message(attacked)
            return

        max_ep = self.karakterek.get_karakter(attacked).max_ep
        sfe = self.karakterek.get_karakter(attacked).sfe

        damage = self.get_damage()
        success, checked_values = validate_values([max_ep, sfe, damage], integers=[0,1,2])

        if not success:
            self.messages.write_message(checked_values)
            return

        [max_ep, sfe, damage] = checked_values

        penalty = return_penalty(sfe, damage, max_ep, attacking_weapon)
        msg = format_damage_msg(penalty)
        self.messages.write_message(msg)