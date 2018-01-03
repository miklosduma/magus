from tkinter import (Button, Entry, Label, W, E,
                     StringVar, VERTICAL, ttk)

from validate import validate_values

FIELD_WIDTH = 10

KARAKTER_PANEL_COLUMN = 0
KARAKTER_PANEL_ROW = 0

NAME_COLUMN = 0
EP_FIELDS_COLUMN = 0
FP_FIELDS_COLUMN = EP_FIELDS_COLUMN + 1
SFE_FIELDS_COLUMN = EP_FIELDS_COLUMN

EP_FRAME_TITLE = 'Eletero'
EP_LABEL = 'Max EP'
FP_LABEL = 'Max FP'
NEV_LABEL = 'Nev'

SFE_FRAME_TITLE = 'SFE'
SFE_LABEL = 'Max SFE'

BUTTONS_FRAME_TITLE = 'Buttons'
ADD_BUTTON = 'Add'
GET_BUTTON = 'Get'

SUCCESS = 'Siker!'
ALREADY_ADDED = '{} mar hozza lett adva.'
NO_CHARACTERS = 'Meg nem adtal hozza karaktert.'
CHARACTERS_ADDED = 'Eddig hozzaadott karakterek: \n{}'


class KarakterPage(ttk.Frame):
    def __init__(self, master, master_gui):
        self.master = master
        self.gui_top = master_gui
        self.karakterek = master_gui.karakterek
        self.messages = master_gui.messages
        ttk.Frame.__init__(self, master)
        self.panels = KarakterPanels(self)
        self.panels.grid(column=0, row=0)


class KarakterPanels(ttk.PanedWindow):
    def __init__(self, master, orient=VERTICAL):
        ttk.PanedWindow.__init__(self, master, orient=orient)
        self.gui_top = master.gui_top
        self.karakterek = self.master.karakterek
        self.messages = self.master.messages
        self.name_frame = NameFrame(self)
        self.fields_frame = FieldsFrame(self)
        self.sfe_frame = SfeFrame(self)
        self.buttons_frame = ButtonsFrame(self)
        self.add(self.name_frame)
        self.add(self.fields_frame)
        self.add(self.sfe_frame)
        self.add(self.buttons_frame)


class NameFrame(ttk.LabelFrame):
    def __init__(self, master):
        self.master = master
        self.gui_top = master.gui_top
        ttk.LabelFrame.__init__(self, master, text=NEV_LABEL)

        self.name_field = CharacterValueField(self)
        self.gui_top.organize_rows_to_left([self.name_field],
                                           NAME_COLUMN)


class FieldsFrame(ttk.LabelFrame):
    def __init__(self, master):
        self.master = master
        self.gui_top = master.gui_top
        ttk.LabelFrame.__init__(self, master, text=EP_FRAME_TITLE)
        self.ep_label = Label(self, text=EP_LABEL)
        self.ep_field = CharacterValueField(self)

        self.fp_field = CharacterValueField(self)
        self.fp_label = Label(self, text=FP_LABEL)

        self.gui_top.organize_rows_to_left([self.ep_label, self.ep_field],
                                           EP_FIELDS_COLUMN)
        self.gui_top.organize_rows_to_left([self.fp_label, self.fp_field],
                                           FP_FIELDS_COLUMN)


class SfeFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=SFE_FRAME_TITLE)
        self.sfe_field = CharacterValueField(self)
        self.master = master
        self.gui_top = master.gui_top
        self.gui_top.organize_rows_to_left([self.sfe_field],
                                           SFE_FIELDS_COLUMN)
        self.fej_sfe = SfePartFrame(self, 'Fej SFE',['homlok', 'koponya'])
        self.fej_sfe.grid(row=3, columnspan=3)


class ButtonsFrame(ttk.LabelFrame):
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=BUTTONS_FRAME_TITLE)
        self.master = master
        self.messages = self.master.messages
        self.add_button = CharacterAddButton(self, ADD_BUTTON,
                                             self.master.karakterek)
        self.get_button = CharactersGetButton(self, GET_BUTTON,
                                              self.master.karakterek)
        self.add_button.grid(column=0, row=0, sticky=W)
        self.get_button.grid(column=1, row=0, sticky=E)


class CharacterAddButton(Button):
    def __init__(self, master, text, karakterek):
        self.master = master
        self.name = self.master.master.name_frame
        self.fields = self.master.master.fields_frame
        self.sfe = self.master.master.sfe_frame
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.add_character)

    def retrieve_values(self):
        values = []
        for field in [self.name.name_field, self.fields.ep_field,
                      self.fields.fp_field, self.sfe.sfe_field]:
            values.append(field.value.get())

        return values

    def add_character(self, event):
        self.sfe.fej_sfe.add_sfe()
        values = self.retrieve_values()
        success, checked_values = validate_values(values, integers=[1,2,3])

        if not success:
            self.messages.write_message(checked_values)
            return

        [name, ep, fp, sfe] = checked_values
        success, msg = self.karakterek.add_karakter(name, ep, sfe, fp=fp)

        if not success:
            msg = ALREADY_ADDED.format(name)

        else:
            msg = SUCCESS

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

        self.master.master.sfe_frame.fej_sfe.get_part_sfe()

        if not all_characters:
            msg = NO_CHARACTERS

        else:
            msg = CHARACTERS_ADDED.format(
                '\n'.join(all_characters))

        self.messages.write_message(msg)


class CharacterValueField(Entry):
    def __init__(self, master, width=FIELD_WIDTH):
        """
        Initialise input field.
        """
        # Varible for entered damage
        self.value = StringVar(master)
        self.value.set('')
        self.value.trace('w', self.print_on_change)

        # Entry field
        Entry.__init__(self, master, textvariable=self.value,
                       width=width)

    def print_on_change(self, *args):
        print(self.value.get())


class SfePartFrame(ttk.LabelFrame):
    def __init__(self, master, text, fields):
        ttk.LabelFrame.__init__(self, master, text=text)
        self.sfe_field = CharacterValueField(self)
        self.master = master
        self.fields = {}
        self.place_sfe_fields(fields)

    def place_sfe_fields(self, fields):
        column = 0
        row = 0
        for field in fields:
            sfe_field = CharacterValueField(self, width=1)
            label = Label(self,text=field)
            sep = Label(self,text='/')
            label.grid(row=row, column=column)
            column += 1
            sfe_field.grid(row=row,column=column, sticky=W)
            column +=1
            sep.grid(row=row, column=column)
            self.fields[field] = sfe_field
            if column >= 3:
                column = 0
                row += 1
            else:
                column += 1

    def get_part_sfe(self):
        for key in self.fields.keys():
            print(key)
            print(self.fields[key])

    def add_sfe(self):
        for key, value in self.fields.items():
            if value.get():
                self.fields[key] = value.get()
