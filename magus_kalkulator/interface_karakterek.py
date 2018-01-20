"""
GUI page for adding new characters.
"""

from tkinter import (Button, Label, W, E, VERTICAL, ttk)

from validate import validate_integer, validate_string, FieldValidationError
from interface_elements import (CharacterValueField, organize_rows_to_left,
                                place_next_in_columns)

KARAKTER_PANEL_COLUMN = 0
KARAKTER_PANEL_ROW = 0

NAME_COLUMN = 0
EP_FIELDS_COLUMN = 0
FP_FIELDS_COLUMN = EP_FIELDS_COLUMN + 1
SFE_FIELDS_COLUMN = EP_FIELDS_COLUMN

PART_SFE_COLUMN_SPAN = 5

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
        self.karakterek = self.master.karakterek
        self.messages = self.master.messages
        self.name_frame = NameFrame(self)
        self.ep_fp_frame = EpFpFrame(self)
        self.sfe_frame = SfeFrame(self)
        self.buttons_frame = ButtonsFrame(self)
        self.add(self.name_frame)
        self.add(self.ep_fp_frame)
        self.add(self.sfe_frame)
        self.add(self.buttons_frame)


class NameFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains
    name field with label.
    """
    def __init__(self, master):
        self.master = master
        ttk.LabelFrame.__init__(self, master, text=NEV_LABEL)

        self.name_field = CharacterValueField(self, validate_string)
        organize_rows_to_left([self.name_field], NAME_COLUMN)


class EpFpFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains
    ep and fp fields with labels.
    """
    def __init__(self, master):
        self.master = master
        ttk.LabelFrame.__init__(self, master, text=EP_FRAME_TITLE)
        self.ep_label = Label(self, text=EP_LABEL)
        self.ep_field = CharacterValueField(self, validate_integer)

        self.fp_label = Label(self, text=FP_LABEL)
        self.fp_field = CharacterValueField(self, validate_integer)

        organize_rows_to_left([self.ep_label, self.ep_field], EP_FIELDS_COLUMN)
        organize_rows_to_left([self.fp_label, self.fp_field], FP_FIELDS_COLUMN)


class SfeFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains the
    main sfe box and all body-part sfe boxes.
    """
    def __init__(self, master):
        ttk.LabelFrame.__init__(self, master, text=SFE_FRAME_TITLE)
        self.master = master
        self.sfe = {}

        Label(self, text=SFE_SHORTCUT_LABEL).grid(row=0,
                                                  column=SFE_FIELDS_COLUMN)
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe_field.grid(row=0, column=SFE_FIELDS_COLUMN + 1)

        self.fej_sfe = SfePartFrame(
            self, SFE_FEJ_LABEL, SFE_FEJ_PARTS)
        self.torzs_sfe = SfePartFrame(
            self, SFE_TORZS_LABEL, SFE_TORZS_PARTS)
        self.kar_sfe = SfePartFrame(self, SFE_KAR_LABEL, SFE_KAR_PARTS,
                                    limb=True)
        self.lab_sfe = SfePartFrame(
            self, SFE_LAB_LABEL, SFE_LAB_PARTS, limb=True)

        place_next_in_columns([self.fej_sfe,
                               self.torzs_sfe,
                               self.kar_sfe,
                               self.lab_sfe],
                              1, SFE_FIELDS_COLUMN, PART_SFE_COLUMN_SPAN)

    def retrieve_sfe_map(self):
        """
        In self.sfe all values are instances of CharacterValueField.
        This method tries to get a validated value from each instance.

        If the validation fails, the method re-raises the validation error.

        On success, a map with integer values is returned.
        """
        return_map = {}
        try:
            for key, value in self.sfe.items():
                value = value.get_validated()
                return_map[key] = value
            return return_map

        except FieldValidationError:
            raise


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
        self.ep_fp = self.master.master.ep_fp_frame
        self.sfe = self.master.master.sfe_frame
        self.karakterek = karakterek
        self.messages = self.master.messages
        Button.__init__(self, master, text=text)
        self.bind('<Button-1>', self.add_character)

    def add_character(self, _event):
        """
        Function executed on clicking Add button.

        Either adds a new character or returns error
        message if validation fails or character already
        exists.
        """
        # Get name, ep and fp fields
        try:
            name = self.name.get_validated()
            ep = self.ep_fp.ep_field.get_validated(min_val=1)
            fp = self.ep_fp.fp_field.get_validated(min_val=1)
            sfe_map = self.sfe.retrieve_sfe_map()

        except FieldValidationError as error:
            self.messages.write_message(error.message)
            return

        # Add exceptional sfe values to map using specified key
        sfe_map = copy_value_to_keys(sfe_map, 'Mellkas', 'Jkulcs', 'Bkulcs')

        # Add new character. Addition fails if character already exists.
        success, msg = self.karakterek.add_karakter(
            name, ep, sfe_map, fp=fp)

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

    def get_characters(self, _event):
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


class SfePartFrame(ttk.LabelFrame):
    """
    Frame child type of main sfe frame. E.g. Fej or Lab frame.
    """
    def __init__(self, master, text, body_parts, limb=False):
        ttk.LabelFrame.__init__(self, master, text=text)
        self.master = master
        self.keys = body_parts

        # Sfe value shortcut that sets all other sfe values
        self.master_sfe = self.master.sfe_field.value
        self.master_sfe.trace('w', self._follow_master)

        Label(self, text=SFE_SHORTCUT_LABEL).grid(row=0, column=0, sticky=W)

        # Sfe shortcut that sets all sfe values listed in body_parts
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe_field.grid(row=0, column=1, sticky=W)
        self.sfe_field.value.trace('w', self._follow_total)

        # Dict attribute holding validated sfe values
        self.sfe_map = self.master.sfe

        if limb:
            self._place_sfe_fields_limb(body_parts)
        else:
            self._place_sfe_fields(body_parts)

    def _follow_master(self, *_args):
        """
        Each child frame has a shortcut value that all
        sub parts follow. E.g. setting Mindenhol in Lab frame
        will change both JLabszar and BBoka to the same value.

        The frame shortcut values however follow a master shortcut value.
        Thus, setting the master value at the top level changes all
        sub-level master values, which in turn change individual sfe values.
        """
        master_value = self.master_sfe.get()
        self.sfe_field.value.set(master_value)

    def _follow_total(self, *_args):
        """
        There is a master shortcut value per body part frame
        that all body parts belonging to that frame follow.
        """
        for key, value in self.sfe_map.items():

            # Only body parts that belong to this frame should follow
            if key in self.keys:
                total = self.sfe_field.value.get()
                value.value.set(total)

            # Match also body parts transformed to start with J/B (right/left)
            elif any(key.lower().endswith(x.lower()) for x in self.keys):
                total = self.sfe_field.value.get()
                value.value.set(total)

    def _place_sfe_fields(self, fields):
        """
        Function to place multiple connected fields assigning
        each a label.
        """
        column = 0
        row = 1

        for field in fields:

            # Place label, it takes its name from the field
            label = Label(self, text=field)
            label.grid(row=row, column=column, sticky=W)

            # Place field next to label
            sfe_field = CharacterValueField(self, validate_integer, width=2)
            sfe_field.grid(row=row, column=column + 1, sticky=W)

            # Add sfe field to sfe map. Sfe field stores the value
            # of the entry field
            self.sfe_map[field] = sfe_field

            # Next label/field will go into next row
            row += 1

    def _place_sfe_fields_limb(self, fields):
        """
        Function to place multiple connected fields assigning
        each a label. Each field value gets a left and right value.
        """
        column = 0
        row = 1

        # Jobb and Bal label added one level higher than fields to the right
        jobb_bal = Label(self, text='Jobb/Bal')
        jobb_bal.grid(row=row, column=column + 1)

        # Place everything below Jobb/Bal label
        row += 1

        for field in fields:

            # Each limb sfe (e.g. Labszar or Boka) is added twice
            # e.g. both as Jlabszar and Blabszar
            jobb_field = 'J{}'.format(field.lower())
            bal_field = 'B{}'.format(field.lower())
            sfe_fields = [jobb_field, bal_field]

            # Add only one label though
            label = Label(self, text=field)
            label.grid(row=row, column=column, sticky=W)

            # Place right and left limb field
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

                # Add sfe field to sfe map. Sfe field stores the value
                # of the entry field
                self.sfe_map[sfe_field] = sfe_field_value

            # Next label/field will go into next row
            row += 1
