from tkinter import (Button, Entry, Label,
                     StringVar, ttk)

import tkMessageBox


class KarakterPage(ttk.Frame):
    def __init__(self, master, karakterek, messages):
        self.karakterek = karakterek
        self.messages = messages
        ttk.Frame.__init__(self, master, width=300, height=600)

        self.add_button = CharacterAddButton(self, 'Add', self.karakterek)
        self.get_button = CharactersGetButton(self, 'Get', self.karakterek)

        self.ep_label = Label(self, text='Max EP')
        self.ep_field = CharacterValueField(self)

        self.fp_field = CharacterValueField(self)
        self.fp_label = Label(self, text='Max FP')

        self.sfe_field = CharacterValueField(self)
        self.sfe_label = Label(self, text='Max SFE')

        self.name_field = CharacterValueField(self)
        self.name_label = Label(self, text='Nev')

        row = 0
        column = 1
        for element in [self.name_label, self.name_field, self.ep_label,
                        self.ep_field, self.fp_label, self.fp_field,
                        self.sfe_label, self.sfe_field, self.add_button,
                        self.get_button]:

            element.grid(column=column, row=row)
            row += 1


class CharacterAddButton(Button):
    def __init__(self, master, text, karakterek):
        self.master = master
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.add_character)

    def retrieve_values(self):
        values = []
        for field in [self.master.name_field, self.master.ep_field,
                      self.master.fp_field, self.master.sfe_field]:
            values.append(field.value.get())

        return values

    def add_character(self, event):
        [name, ep, fp, sfe] = self.retrieve_values()
        success, msg = self.karakterek.add_karakter(name, int(ep),
                                                    int(sfe), fp=int(fp))

        if not success:
            msg = '{} mar hozza lett adva.'.format(name)

        else:
            msg = 'Siker!'

        self.messages.write_message(msg)

class CharactersGetButton(Button):
    def __init__(self, master, text, karakterek):
        self.karakterek = karakterek
        Button.__init__(self, master, text=text)
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

    def print_on_change(self, *args):
        print(self.value.get())