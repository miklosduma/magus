from tkinter import (Button, Entry, Label, W, E, N,
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
    def __init__(self, master, master_gui, width):
        self.master = master
        self.gui_top = master_gui
        self.karakterek = master_gui.karakterek
        self.messages = master_gui.messages
        ttk.Frame.__init__(self, master, width=width)
        self.panels = KarakterPanels(self, width)
        self.panels.grid(column=0, row=0, columnspan=8)


class KarakterPanels(ttk.PanedWindow):
    def __init__(self, master, width, orient=VERTICAL):
        ttk.PanedWindow.__init__(self, master, width=width, orient=orient)
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
        self.fej_sfe = SfePartFrame(self, 'Fej SFE',['Homlok', 'Koponya', 'Arc'])
        self.fej_sfe.grid(row=3, columnspan=5, sticky=(N,W))

        self.torzs_sfe = SfePartFrame(self, 'Torzs SFE', ['Mellkas', 'Has', 'Vallak'])
        self.torzs_sfe.grid(row=3, column=5, columnspan=5,sticky=(N,W))

        self.kar_sfe = SfePartFrame(self, 'Kar SFE', ['Felkar', 'Alkar', 'Kezfej'], limb=True)
        self.kar_sfe.grid(row=4, columnspan=5, sticky=(N,W))

        self.lab_sfe = SfePartFrame(self, 'Lab SFE', ['Comb', 'Terd', 'Labszar', 'Labfej'], limb=True)
        self.lab_sfe.grid(row=4, column =5, columnspan=5, sticky=(N,W))


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
        self.master.master.sfe_frame.lab_sfe.get_part_sfe()

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
    def __init__(self, master, text, fields, limb=False):
        ttk.LabelFrame.__init__(self, master, text=text)
        self.is_limb = limb
        self.sfe_field = CharacterValueField(self, width=2)
        Label(self, text='Total').grid(row=0, column=0, sticky=W)
        self.sfe_field.grid(row=0, column=1, sticky=E)
        self.master = master
        self.fields = {}
        self.place_sfe_fields(fields)
        self.sfe_field.value.trace('w', self.follow_total)

    def follow_total(self, *_args):
        for value in self.fields.values():
            total = self.sfe_field.value.get()
            value.value.set(total)

    def place_sfe_fields(self, fields):
        column = 0
        row = 1

        if self.is_limb:
            jobb_bal = Label(self, text='Jobb/Bal')
            jobb_bal.grid(row=row, column=column + 1)
            row += 1

        for field in fields:

            if self.is_limb:
                jobb_field = 'J{}'.format(field.lower())
                bal_field = 'B{}'.format(field.lower())
                sfe_fields = [jobb_field, bal_field]
            else:
                sfe_fields = [field]

            label = Label(self, text=field)
            label.grid(row=row, column=column, sticky=W)

            for sfe_field in sfe_fields:
                sfe_field_value = CharacterValueField(self, width=2)

                if sfe_fields.index(sfe_field) == 0:
                    direction = W
                else:
                    direction = E

                sfe_field_value.grid(row=row,column=column+1, sticky=direction)
                self.fields[sfe_field] = sfe_field_value

            row += 1

    def get_part_sfe(self):
        for key in self.fields.keys():
            print(key)
            print(self.fields[key].value.get())

    def add_sfe(self):
        for key, value in self.fields.items():
            if value.get():
                self.fields[key] = value.get()
