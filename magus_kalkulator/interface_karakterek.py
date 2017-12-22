from tkinter import (Button, Entry, Label, W, E,
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
                        self.sfe_label, self.sfe_field]:

            element.grid(column=column, row=row, sticky=W)
            row += 1
        self.add_button.grid(column=column, row=row, sticky=W)
        self.get_button.grid(column=column, row=row, sticky=E)


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

    def validate_values(self, values):
        [name, ep, fp, sfe] = values
        missing = [x for x in values if not x]

        if missing:
            return False, 'Tolts ki minden mezot!'

        try:
            ep = int(ep)
            fp = int(fp)
            sfe = int(sfe)
        except ValueError as error:
            return False, 'Nem szam: {}'.format(error.message)

        return True, [name, ep, fp, sfe]

    def add_character(self, event):
        values = self.retrieve_values()
        success, checked_values = self.validate_values(values)

        if not success:
            self.messages.write_message(checked_values)
            return

        [name, ep, fp, sfe] = checked_values
        success, msg = self.karakterek.add_karakter(name, ep, sfe, fp=fp)

        if not success:
            msg = '{} mar hozza lett adva.'.format(name)

        else:
            msg = 'Siker!'

        self.messages.write_message(msg)


class CharactersGetButton(Button):
    def __init__(self, master, text, karakterek):
        self.master = master
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.get_characters)

    def get_characters(self, event):
        all_characters = self.karakterek.get_all_karakters()

        if not all_characters:
            msg = 'Meg nem adtal hozza karaktert.'

        else:
            msg = 'Eddig hozzaadott karakterek: \n{}'.format(
                '\n'.join(all_characters))

        self.messages.write_message(msg)


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