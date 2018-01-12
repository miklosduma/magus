from tkinter import (Button, Entry, Label, W, E, N,
                     StringVar, VERTICAL, ttk)

from validate import validate_integer, validate_string


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


def collect_field_values(root, values=[]):

    children = root.winfo_children()

    if not children:
        return values

    for child in children:

        if 'get' in dir(child):
            values.append(child.get())

        if child.winfo_children():
            collect_field_values(child, values=values)

    return values


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

        self.name_field = CharacterValueField(self, validate_string)
        self.gui_top.organize_rows_to_left([self.name_field],
                                           NAME_COLUMN)


class FieldsFrame(ttk.LabelFrame):

    def __init__(self, master):
        self.master = master
        self.gui_top = master.gui_top
        ttk.LabelFrame.__init__(self, master, text=EP_FRAME_TITLE)
        self.ep_label = Label(self, text=EP_LABEL)
        self.ep_field = CharacterValueField(self, validate_integer)

        self.fp_field = CharacterValueField(self, validate_integer)
        self.fp_label = Label(self, text=FP_LABEL)

        self.gui_top.organize_rows_to_left([self.ep_label, self.ep_field],
                                           EP_FIELDS_COLUMN)
        self.gui_top.organize_rows_to_left([self.fp_label, self.fp_field],
                                           FP_FIELDS_COLUMN)


class SfeFrame(ttk.LabelFrame):

    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=SFE_FRAME_TITLE)
        self.sfe_label = Label(self, text='Mindenhol')
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe = {}
        self.master = master
        self.sfe_label.grid(row=0)
        self.sfe_field.grid(row=0, column=1)

        self.fej_sfe = SfePartFrame(
            self, 'Fej SFE', ['Arc', 'Nyak', 'Koponya'])
        self.fej_sfe.grid(row=3, columnspan=5, sticky=(N, W))

        self.torzs_sfe = SfePartFrame(
            self, 'Torzs SFE', ['Mellkas', 'Has', 'Agyek'])
        self.torzs_sfe.grid(row=3, column=5, columnspan=5, sticky=(N, W))

        self.kar_sfe = SfePartFrame(self, 'Kar SFE', ['Vall', 'Felkar', 'Konyok', 'Alkar', 'Csuklo', 'Kezfej'],
                                    limb=True)
        self.kar_sfe.grid(row=4, columnspan=5, sticky=(N, W))

        self.lab_sfe = SfePartFrame(
            self, 'Lab SFE', ['Comb', 'Terd', 'Labszar', 'Boka', 'Labfej'], limb=True)
        self.lab_sfe.grid(row=4, column=5, columnspan=5, sticky=(N, W))


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
        self.name = self.master.master.name_frame.name_field
        self.fields = self.master.master.fields_frame
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.add_character)

    def add_character(self, event):
        sfe_map = self.master.master.sfe_frame.sfe

        new_sfe_map = {}
        for key, sfe_field in sfe_map.items():
            success, value = sfe_field.validate()

            if not success:
                self.messages.write_message(value)
                return
            else:
                new_sfe_map[key] = value

        name_field = self.name
        ep_field = self.fields.ep_field
        fp_field = self.fields.fp_field

        values = []
        for field in [name_field, ep_field, fp_field]:
            success, value = field.validate()

            if not success:
                self.messages.write_message(value)
                return
            else:
                values.append(value)

        [name, ep, fp] = values

        success, msg = self.karakterek.add_karakter(
            name, ep, new_sfe_map, fp=fp)

        if not success:
            msg = ALREADY_ADDED.format(name)

        else:
            msg = SUCCESS
            new_char = self.karakterek.get_karakter(name)
            print(new_char.max_ep, new_char.max_fp, new_char.sfe)

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

    def __init__(self, master, validate_fun, width=FIELD_WIDTH):
        """
        Initialise input field.
        """
        # Varible for entered damage
        self.value = StringVar(master)
        self.value.set('')
        self.value.trace('w', self.print_on_change)
        self.validator = validate_fun

        # Entry field
        Entry.__init__(self, master, textvariable=self.value,
                       width=width)

    def print_on_change(self, *args):
        color = self.cget('bg')

        if color == 'red':
            self.config(bg='white')

        print(self.value.get())

    def validate(self):
        success, value = self.validator(self.value.get())

        if not success:
            self.config(bg='red')
        return success, value


class SfePartFrame(ttk.LabelFrame):

    def __init__(self, master, text, fields, limb=False):
        ttk.LabelFrame.__init__(self, master, text=text)
        self.is_limb = limb
        self.keys = fields
        self.master = master
        self.total_sfe = self.master.sfe_field.value
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        Label(self, text='Total').grid(row=0, column=0, sticky=W)
        self.sfe_field.grid(row=0, column=1, sticky=W)
        self.master = master
        self.fields = self.master.sfe
        self.local_fields = []
        self.place_sfe_fields(fields)
        self.total_sfe.trace('w', self.follow_master)
        self.sfe_field.value.trace('w', self.follow_total)

    def follow_master(self, *_args):
        self.sfe_field.value.set(self.total_sfe.get())

    def follow_total(self, *_args):
        for key, value in self.fields.items():

            if key in self.local_fields:
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
                sfe_field_value = CharacterValueField(
                    self, validate_integer, width=2)

                if sfe_fields.index(sfe_field) == 0:
                    direction = W
                else:
                    direction = E

                sfe_field_value.grid(
                    row=row, column=column + 1, sticky=direction)
                self.fields[sfe_field] = sfe_field_value
                self.local_fields.append(sfe_field)

            row += 1

    def get_part_sfe(self):
        values = []

        for key in self.fields.keys():
            values.append(self.fields[key].value.get())
        return values

    def add_sfe(self):
        for key, value in self.fields.items():
            if 'get' not in dir(value):
                print(dir(value))
            elif value.get():
                self.fields[key] = value.get()
