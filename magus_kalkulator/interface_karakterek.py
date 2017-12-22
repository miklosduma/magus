from tkinter import (Button, Entry, Label, W, E,
                     StringVar, VERTICAL, ttk)

import tkMessageBox


class KarakterPage(ttk.Frame):
    def __init__(self, master, karakterek, messages):
        self.karakterek = karakterek
        self.messages = messages
        ttk.Frame.__init__(self, master, width=300, height=600)
        self.panels = KarakterPanels(self)
        self.panels.grid(column=0, row=0)


class KarakterPanels(ttk.PanedWindow):
    def __init__(self, master, orient=VERTICAL):
        ttk.PanedWindow.__init__(self, master, orient=orient)
        self.karakterek = self.master.karakterek
        self.messages = self.master.messages
        self.fields_frame = FieldsFrame(self)
        self.sfe_frame = SfeFrame(self)
        self.buttons_frame = ButtonsFrame(self)
        self.add(self.fields_frame)
        self.add(self.sfe_frame)
        self.add(self.buttons_frame)


class FieldsFrame(ttk.LabelFrame):
    def __init__(self, master):
        self.master = master
        ttk.LabelFrame.__init__(self, master, height=100, width=100,
                                text='Eletero')
        self.ep_label = Label(self, text='Max EP')
        self.ep_field = CharacterValueField(self)

        self.fp_field = CharacterValueField(self)
        self.fp_label = Label(self, text='Max FP')

        self.name_field = CharacterValueField(self)
        self.name_label = Label(self, text='Nev')

        row = 0
        column = 1
        for element in [self.name_label, self.name_field, self.ep_label,
                        self.ep_field, self.fp_label, self.fp_field]:
            element.grid(column=column, row=row, sticky=W)
            row += 1

class SfeFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, height=100, width=100, text='SFE')
        self.sfe_field = CharacterValueField(self)
        self.sfe_label = Label(self, text='Max SFE')
        self.master = master
        row = 0
        column = 1
        for element in [self.sfe_label, self.sfe_field]:
            element.grid(column=column, row=row, sticky=W)
            row += 1


class ButtonsFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, height=100, width=100, text='Buttons')
        self.master = master
        self.messages = self.master.messages
        self.add_button = CharacterAddButton(self, 'Add', self.master.karakterek)
        self.get_button = CharactersGetButton(self, 'Get', self.master.karakterek)
        self.add_button.grid(column=0, row=0, sticky=W)
        self.get_button.grid(column=1, row=0, sticky=E)


class CharacterAddButton(Button):
    def __init__(self, master, text, karakterek):
        self.master = master
        self.fields = self.master.master.fields_frame
        self.sfe = self.master.master.sfe_frame
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.add_character)

    def retrieve_values(self):
        values = []
        for field in [self.fields.name_field, self.fields.ep_field,
                      self.fields.fp_field, self.sfe.sfe_field]:
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