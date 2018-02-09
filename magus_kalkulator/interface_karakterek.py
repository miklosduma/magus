"""
GUI page for adding new characters.
"""

from tkinter import Button, Label, W, E, VERTICAL, ttk

from magus_kalkulator.validate import (validate_integer, validate_string,
                                       FieldValidationError)
from magus_kalkulator.interface_elements import (CharacterValueField,
                                                 SfePartFrame,
                                                 organize_rows_to_left,
                                                 place_next_in_columns)
import magus_kalkulator.magus_constants as mgc

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

RIGHT_LEFT_LABEL = 'Jobb/Bal'

SFE_SHORTCUT_LABEL = 'Mindenhol'

SFE_FEJ_LABEL = 'Fej SFE'
SFE_FEJ_PARTS = [mgc.FACE, mgc.NECK, mgc.SKULL]

SFE_TORZS_LABEL = 'Torzs SFE'
SFE_TORZS_PARTS = [mgc.CHEST, mgc.STOMACH, mgc.GROINS]

# Each from behind torso part references a from front torso part,
# taking the front part's SFE
SFE_TORZS_PARTS_BEHIND = [(mgc.SHOULDERBLADE, mgc.CHEST),
                          (mgc.BACK, mgc.CHEST),
                          (mgc.WAIST, mgc.STOMACH),
                          (mgc.BUTTOCKS, mgc.GROINS),
                          (mgc.SPINE_UPPER, mgc.CHEST),
                          (mgc.SPINE_LOWER, mgc.STOMACH)]


SFE_KAR_LABEL = 'Kar SFE'
SFE_KAR_PARTS = [('Vall', mgc.RSHOULDSERS, mgc.LSHOULDSERS),
                 ('Felkar', mgc.RUPPERARM, mgc.LUPPERARM),
                 ('Konyok', mgc.RELBOW, mgc.LELBOW),
                 ('Alkar', mgc.RLOWERARM, mgc.LLOWERARM),
                 ('Csuklo', mgc.RWRIST, mgc.LWRIST),
                 ('Kezfej', mgc.RHAND, mgc.LHAND)]

SFE_LAB_LABEL = 'Lab SFE'
SFE_LAB_PARTS = [('Comb', mgc.RTHIGH, mgc.LTHIGH),
                 ('Terd', mgc.RKNEE, mgc.LKNEE),
                 ('Labszar', mgc.RSHIN, mgc.LSHIN),
                 ('Boka', mgc.RANKLE, mgc.LANKLE),
                 ('Labfej', mgc.RFOOT, mgc.LFOOT)]

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


def insert_torso_back_armour(sfe_map):
    """
    Inserts all the back torso armour values into the
    armour map using a constant list.

    The constant list is made up of tuples, where
    the first element of the tuple is the new key to be
    inserted, the second element is the existing key whose
    value the new key will take.
    """
    for new_key, key in SFE_TORZS_PARTS_BEHIND:
        sfe_map = copy_value_to_keys(sfe_map, key, new_key)

    return sfe_map


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

        self.fej_sfe = SfePartFrame(self, SFE_FEJ_LABEL,
                                    SFE_SHORTCUT_LABEL, SFE_FEJ_PARTS)
        self.torzs_sfe = SfePartFrame(self, SFE_TORZS_LABEL,
                                      SFE_SHORTCUT_LABEL, SFE_TORZS_PARTS)
        self.kar_sfe = SfePartFrameLimb(self, SFE_SHORTCUT_LABEL,
                                        SFE_KAR_LABEL, SFE_KAR_PARTS)
        self.lab_sfe = SfePartFrameLimb(self, SFE_SHORTCUT_LABEL,
                                        SFE_LAB_LABEL, SFE_LAB_PARTS)

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
            max_ep = self.ep_fp.ep_field.get_validated(min_val=1)
            max_fp = self.ep_fp.fp_field.get_validated(min_val=1)
            sfe_map = self.sfe.retrieve_sfe_map()

        except FieldValidationError as error:
            self.messages.write_message(error.message)
            return

        # Add exceptional sfe values to map using specified key
        sfe_map = copy_value_to_keys(sfe_map, mgc.CHEST, mgc.RCOLLARBONE,
                                     mgc.LCOLLARBONE)
        sfe_map = insert_torso_back_armour(sfe_map)

        # Add new character. Addition fails if character already exists.
        success, msg = self.karakterek.add_karakter(
            name, max_ep, sfe_map, fp=max_fp)

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


class SfePartFrameNotLimb(SfePartFrame):
    """
    Frame child type of main sfe frame. E.g. Torso or Head frame.
    """
    def __init__(self, master, text, body_parts):
        SfePartFrame.__init__(self, master, text, SFE_SHORTCUT_LABEL,
                              body_parts)


class SfePartFrameLimb(SfePartFrame):
    """
    Frame child type of main sfe frame. E.g. Fej or Lab frame.
    """
    def __init__(self, master, text, shortcut_text, body_parts):
        SfePartFrame.__init__(self, master, text, shortcut_text, body_parts)

    def _sort_body_parts(self, body_parts):
        """
        In the case of limbs, body_parts are a list of tuples,
        each comprising: a label text, a right and a left limb.
        """
        result = []
        for bp_tuple in body_parts:
            _text, right_part, left_part = bp_tuple
            result.append(right_part)
            result.append(left_part)
        return result

    def _place_sfe_fields(self, fields):
        """
        Overrides the same method of SfePartFrame. Since we
        have both right and left limbs.
        """
        column = 0
        row = 1

        # Jobb and Bal label added one level higher than fields to the right
        jobb_bal = Label(self, text=RIGHT_LEFT_LABEL)
        jobb_bal.grid(row=row, column=column + 1)

        # Place everything below Jobb/Bal label
        row += 1

        for field in fields:
            label_text, right_part, left_part = field

            # Each limb sfe (e.g. Labszar or Boka) is added twice
            # e.g. both as Jlabszar and Blabszar
            sfe_fields = [right_part, left_part]

            # Add only one label though
            label = Label(self, text=label_text)
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
