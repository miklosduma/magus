from tkinter import (Tk, Button, Frame, N, W, E, S, Entry,
                     StringVar, OptionMenu, Label, mainloop, ttk, Canvas)

class KarakterPage(ttk.Frame):
    def __init__(self, master, karakterek):
        self.karakterek = karakterek
        ttk.Frame.__init__(self, master, width=300, height=600)
        self.add_button = CharacterAddButton(self, 'Add', self.karakterek)
        self.get_button = CharactersGetButton(self, 'Get', self.karakterek)


class CharacterAddButton(Button):
    def __init__(self, master, text, karakterek):
        self.karakterek = karakterek
        Button.__init__(self, master, text=text)
        self.place(relx=.5, rely=.75, anchor='center')
        self.bind('<Button-1>', self.add_character)

    def add_character(self, event):
        self.karakterek.add_karakter('Vimes', 14, 5)


class CharactersGetButton(Button):
    def __init__(self, master, text, karakterek):
        self.karakterek = karakterek
        Button.__init__(self, master, text=text)
        self.place(relx=.3, rely=.75, anchor='center')
        self.bind('<Button-1>', self.get_characters)

    def get_characters(self, event):
        print(self.karakterek.get_all_karakters())