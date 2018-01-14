from tkinter import (Button, Entry, Label, W, E, N,
                     StringVar, VERTICAL, ttk)

from validate import validate_integer, validate_string


FIELD_WIDTH = 10
FIELD_COLOR = 'white'
FIELD_COLOR_ERROR = 'red'

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

SFE_SHORTCUT_LABEL = 'Mindenhol'

SFE_FEJ_LABEL = 'Fej SFE'
SFE_FEJ_PARTS = ['Arc', 'Nyak', 'Koponya']

SFE_TORZS_LABEL = 'Torzs SFE'
SFE_TORZS_PARTS = ['Mellkas', 'Has', 'Agyek']

SFE_KAR_LABEL = 'Kar SFE'
SFE_KAR_PARTS = ['Vall', 'Felkar', 'Konyok', 'Alkar', 'Csuklo', 'Kezfej']

SFE_LAB_LABEL = 'Lab SFE'
SFE_LAB_PARTS = ['Comb', 'Terd', 'Labszar', 'Boka', 'Labfej']

BUTTONS_FRAME_TITLE = 'Buttons'
ADD_BUTTON = 'Add'
GET_BUTTON = 'Get'

SUCCESS = 'Siker!'
ALREADY_ADDED = '{} mar hozza lett adva.'
NO_CHARACTERS = 'Meg nem adtal hozza karaktert.'
CHARACTERS_ADDED = 'Eddig hozzaadott karakterek: \n{}'


def copy_value_to_keys(my_map, key, *new_keys):
    """
    Takes a map and inserts all specified new keys. The value
    of the new keys matches the value that corresponds to 'key'.

    Returns the new map.
    """
    value = my_map[key]

    for new_key in new_keys:
        my_map[new_key] = value

    return my_map


class KarakterPage(ttk.Frame):
    """
    Adding characters main page.
    """
    def __init__(self, master, master_gui, width):
        self.master = master
        self.gui_top = master_gui
        self.karakterek = master_gui.karakterek
        self.messages = master_gui.messages
        ttk.Frame.__init__(self, master, width=width)
        self.panels = KarakterPanels(self, width)
        self.panels.grid(column=0, row=0, columnspan=8)


class KarakterPanels(ttk.PanedWindow):
    """
    Main panel of characters main page.
    """
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
    """
    Part of characters panel. Contains
    name field with label.
    """
    def __init__(self, master):
        self.master = master
        self.gui_top = master.gui_top
        ttk.LabelFrame.__init__(self, master, text=NEV_LABEL)

        self.name_field = CharacterValueField(self, validate_string)
        self.gui_top.organize_rows_to_left([self.name_field],
                                           NAME_COLUMN)


class FieldsFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains
    ep and fp fields with labels.
    """
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
    """
    Part of characters panel. Contains the
    main sfe box and all body-part sfe boxes.
    """
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=SFE_FRAME_TITLE)
        self.sfe_label = Label(self, text=SFE_SHORTCUT_LABEL)
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe = {}
        self.master = master
        self.sfe_label.grid(row=0)
        self.sfe_field.grid(row=0, column=1)

        self.fej_sfe = SfePartFrame(
            self, SFE_FEJ_LABEL, SFE_FEJ_PARTS)
        self.fej_sfe.grid(row=3, columnspan=5, sticky=(N, W))

        self.torzs_sfe = SfePartFrame(
            self, SFE_TORZS_LABEL, SFE_TORZS_PARTS)
        self.torzs_sfe.grid(row=3, column=5, columnspan=5, sticky=(N, W))

        self.kar_sfe = SfePartFrame(self, SFE_KAR_LABEL, SFE_KAR_PARTS,
                                    limb=True)
        self.kar_sfe.grid(row=4, columnspan=5, sticky=(N, W))

        self.lab_sfe = SfePartFrame(
            self, SFE_LAB_LABEL, SFE_LAB_PARTS, limb=True)
        self.lab_sfe.grid(row=4, column=5, columnspan=5, sticky=(N, W))


class ButtonsFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains buttons.
    """
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
    """
    Adds new character on clicking.
    """
    def __init__(self, master, text, karakterek):
        self.master = master
        self.name = self.master.master.name_frame.name_field
        self.fields = self.master.master.fields_frame
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.add_character)

    def add_character(self, event):
        """
        Function executed on clicking Add button.

        Either adds a new character or returns error
        message if validation fails or character already
        exists.
        """

        # Get sfe fields from sfe frame
        sfe_map = self.master.master.sfe_frame.sfe

        # Build sfe map from fields. If any field fails
        # validation the character is not added
        new_sfe_map = {}
        for key, sfe_field in sfe_map.items():
            success, value = sfe_field.validate()

            # Handle validation failures
            if not success:
                self.messages.write_message(value)
                return

            # Add field's current value to sfe map
            else:
                new_sfe_map[key] = value

        # Kulcscsontok mellkas pancelt hasznaljak
        new_sfe_map = copy_value_to_keys(new_sfe_map,
                                         'Mellkas', 'Jkulcs', 'Bkulcs')

        # Get name, ep and fp fields
        name_field = self.name
        ep_field = self.fields.ep_field
        fp_field = self.fields.fp_field

        # Validate each, and add their values to list
        values = []
        for field in [name_field, ep_field, fp_field]:
            success, value = field.validate()

            if not success:
                self.messages.write_message(value)
                return
            else:
                values.append(value)

        [name, ep, fp] = values

        # Add new character. Addition fails if character already exists.
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
    """
    Button that lists all characters already added.
    """
    def __init__(self, master, text, karakterek):
        self.master = master
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.get_characters)

    def get_characters(self, event):
        """
        Function executed on clicking Get button.
        Lists all characters already added.
        """
        all_characters = self.karakterek.get_all_karakters()

        if not all_characters:
            msg = NO_CHARACTERS

        else:
            msg = CHARACTERS_ADDED.format(
                '\n'.join(all_characters))

        self.messages.write_message(msg)


class CharacterValueField(Entry):
    """
    Basic field type used to store character values.
    """
    def __init__(self, master, validate_fun, width=FIELD_WIDTH):
        """
        Initialise input field.
         - validate_fun:
            A function used to validate the field's input value.
        """
        # Varible for entered value
        self.value = StringVar(master)
        self.value.set('')
        self.value.trace('w', self.follow_changes)
        self.validator = validate_fun

        # Entry field
        Entry.__init__(self, master, textvariable=self.value,
                       width=width)

    def follow_changes(self, *args):
        """
        Traces changes to the input value
        of the field.
        """
        # Get current background color of field.
        color = self.cget('bg')

        # It turns red on validation failures.
        # Any subsequent change must turn the color back
        # to the default color.
        if color == FIELD_COLOR_ERROR:
            self.config(bg=FIELD_COLOR)

        print(self.value.get())

    def validate(self):
        """
        Calls assigned validator function on the
        value of the field.

        If validation fails, turns the field to red.
        """
        success, value = self.validator(self.value.get())

        if not success:
            self.config(bg=FIELD_COLOR_ERROR)
        return success, value


class SfePartFrame(ttk.LabelFrame):
    """
    Frame child type of main sfe frame. E.g. Fej or Lab frame.
    """
    def __init__(self, master, text, fields, limb=False):
        ttk.LabelFrame.__init__(self, master, text=text)
        self.is_limb = limb
        self.keys = fields
        self.master = master
        self.total_sfe = self.master.sfe_field.value
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        Label(self, text=SFE_SHORTCUT_LABEL).grid(row=0, column=0, sticky=W)
        self.sfe_field.grid(row=0, column=1, sticky=W)
        self.master = master
        self.fields = self.master.sfe
        self.local_fields = []
        self.place_sfe_fields(fields)
        self.total_sfe.trace('w', self.follow_master)
        self.sfe_field.value.trace('w', self.follow_total)

    def follow_master(self, *_args):
        """
        Each child frame has a shortcut value that all
        sub parts follow. E.g. setting Mindenhol in Lab frame
        will change both JLabszar and BBoka to the same value.
        """
        self.sfe_field.value.set(self.total_sfe.get())

    def follow_total(self, *_args):
        """
        There is a master shortcut value that all other
        fields follow. Setting the value of it changes
        all other sfe field values.
        """
        for key, value in self.fields.items():

            if key in self.local_fields:
                total = self.sfe_field.value.get()
                value.value.set(total)

    def place_sfe_fields(self, fields):
        """
        Function to place multiple connected fields assigning
        each a label.
        """
        column = 0
        row = 1

        # If field is a limb sfe (e.g. Labszar or Boka)
        # Jobb and Bal label will be added
        if self.is_limb:
            jobb_bal = Label(self, text='Jobb/Bal')
            jobb_bal.grid(row=row, column=column + 1)
            row += 1

        for field in fields:

            # If field is a limb sfe (e.g. Labszar or Boka)
            # it will be added twice both as Jlabszar and Blabszar
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

                # Right (jobb) limbs are left aligned,
                # left (bal) limbs are right aligned
                if sfe_fields.index(sfe_field) == 0:
                    direction = W
                else:
                    direction = E

                sfe_field_value.grid(
                    row=row, column=column + 1, sticky=direction)
                self.fields[sfe_field] = sfe_field_value
                self.local_fields.append(sfe_field)

            row += 1
