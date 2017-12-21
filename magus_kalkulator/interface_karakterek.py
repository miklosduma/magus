from tkinter import (Tk, Button, Frame, N, W, E, S, Entry,
                     StringVar, OptionMenu, Label, mainloop, ttk, Canvas)

import tkMessageBox

class KarakterPage(ttk.Frame):
    def __init__(self, master, karakterek):
        self.karakterek = karakterek
        ttk.Frame.__init__(self, master, width=300, height=600)
        self.add_button = CharacterAddButton(self, 'Add', self.karakterek)
        self.get_button = CharactersGetButton(self, 'Get', self.karakterek)
        # self.ep_field = CharacterValueField(self)


class CharacterAddButton(Button):
    def __init__(self, master, text, karakterek):
        self.karakterek = karakterek
        Button.__init__(self, master, text=text)
        self.grid(column=1, row=4)
        self.bind('<Button-1>', self.add_character)

    def add_character(self, event):
        success, msg = self.karakterek.add_karakter('Vimes', 14, 5)

        if not success:
            tkMessageBox.showwarning('Nem ezeket a droidokat keresik!', msg)
        else:
            tkMessageBox.showinfo('Siker!', msg)



class CharactersGetButton(Button):
    def __init__(self, master, text, karakterek):
        self.karakterek = karakterek
        Button.__init__(self, master, text=text)
        self.grid(column=2, row=4)
        self.bind('<Button-1>', self.get_characters)

    def get_characters(self, event):
        print(self.karakterek.get_all_karakters())


class CharacterValueField(Entry):
    def __init__(self, master):
        """
        Initialise input field.
        """
        # Varible for entered damage
        self.value = StringVar(master)
        self.value.set('')
        self.value.trace('w', self.print_on_change)

        # Entry field
        Entry.__init__(self, master, textvariable=self.value)
        self.grid(row=6, column=1)

    def print_on_change(self, *args):
        print(self.value.get())