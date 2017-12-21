from tkinter import (Entry, StringVar, OptionMenu, ttk)


# Types of attacking weapons. Used when calculating the damage
WEAPON_TYPES = ['Szur', 'Vag', 'Zuz', 'Harap', 'Karmol']


class SebzesPage(ttk.Frame):
    """
    Main tab for calculating damage and penalties.
    """
    def __init__(self, master, karakterek):
        """
        Initializes damage tab.
        """
        ttk.Frame.__init__(self, master, width=300, height=600)

        # Variable for character selection drop-down
        # SFE and Max_EP of character is used when calculating damage
        self.karakter_var = KarakterVar(self)
        self.karakterek = karakterek
        self.dropdown = KarakterekMenu(self, self.karakter_var,
                                       self.karakterek, *["1", "2", "3"])

        # Variable for type of attacking weapon. Can be selected from drop-down
        self.weapon_type = WeaponString(self, WEAPON_TYPES)
        self.weapon_menu = WeaponTypeMenu(self, self.weapon_type, *WEAPON_TYPES)

        # Variable for total damage. Can be entered into entry field
        self.sebzes = SebzesField(self)


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
        self.grid(row=6, column=1)

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
        self.grid(row=4, column=1)


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
    def __init__(self, master):
        """
        Initialise variable.
        """
        StringVar.__init__(self, master)
        self.set_value('')
        self.master = master
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
        return self.get()

    def print_on_change(self, *args):
        """
        Print latest value and max_ep of
        selected character.
        """
        print(self.get_value())
        print(self.master.master.karakterek.get_karakter(
            self.get_value()).max_ep)

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
        self.grid(row=2, column=1)
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