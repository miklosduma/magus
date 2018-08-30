"""
GUI page for adding new characters.
"""

from tkinter import Button, Label, W, E, VERTICAL, ttk, IntVar, Checkbutton

from magus_kalkulator.validate import (validate_integer, validate_string,
                                       FieldValidationError)
from magus_kalkulator.interface_elements import (CharacterValueField,
                                                 organize_rows_to_left,
                                                 place_next_in_columns,
                                                 on_all_children,
                                                 save_characters,
                                                 collect_children_type_of)
import magus_kalkulator.magus_constants as mgc

KARAKTER_PANEL_COLUMN = 0
KARAKTER_PANEL_ROW = 0

NAME_COLUMN = 0
EP_FIELDS_COLUMN = 0
FP_FIELDS_COLUMN = EP_FIELDS_COLUMN + 1
SFE_FIELDS_COLUMN = EP_FIELDS_COLUMN

PART_SFE_COLUMN_SPAN = 5

EP_FRAME_TITLE = 'Eletero'
EP_LABEL = 'EP'
FP_LABEL = 'FP'
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


def place_max_act_fields(frame, max_field, act_field,
                         label_text=None, start_row=0, start_column=0):

    if label_text:
        Label(frame, text=label_text).grid(column=start_column, row=start_row)
        start_column += 1

    max_field.grid(column=start_column, row=start_row)
    start_column += 1

    Label(frame, text='/').grid(column=start_column, row=start_row)
    start_column += 1

    act_field.grid(column=start_column, row=start_row)
    start_column += 1

    return start_column


class KarakterPage(ttk.Frame):
    """
    Adding characters main page.
    """
    def __init__(self, tabs_master, characters, messages, width):

        self.characters = characters
        self.messages = messages

        ttk.Frame.__init__(self, tabs_master, width=width)
        self.panels = KarakterPanels(self, width)
        self.panels.grid(column=0, row=1, columnspan=8)

        add_button = Button(self, text=ADD_BUTTON)
        add_button.bind('<Button-1>', self.panels.add_character)
        add_button.grid(column=0, row=2, sticky=W)

        get_button = Button(self, text=GET_BUTTON)
        get_button.bind('<Button-1>', self.panels.get_characters)
        get_button.grid(column=0, row=2, sticky=E)

    def reset_page(self):
        """
        Resets all the child widgets of the page.
        """
        self.panels.reset_panel()


class KarakterPanels(ttk.PanedWindow):
    """
    Main panel of characters main page.
    """
    def __init__(self, character_page, width, orient=VERTICAL):
        ttk.PanedWindow.__init__(self, character_page,
                                 width=width, orient=orient)
        self.character_page = character_page

        self.name_frame = NameFrame(self)
        self.add(self.name_frame)

        self.ep_fp_frame = EpFpFrame(self)
        self.add(self.ep_fp_frame)

        self.sfe_frame = SfeFrame(self)
        self.add(self.sfe_frame)

    def reset_panel(self):
        """
        Resets all the child widgets of the panel.
        """
        on_all_children('reset_frame', self)

    def get_characters(self, *_args):
        """
        Function executed on clicking Get button.
        Lists all characters already added.
        """
        all_characters = \
            self.character_page.characters.get_character_names()

        if not all_characters:
            msg = NO_CHARACTERS

        else:
            msg = CHARACTERS_ADDED.format(
                '\n'.join(all_characters))

        self.character_page.messages.write_message(msg)

    def add_character(self, *_args):
        """
        Function executed on clicking Add button.

        Either adds a new character or returns error
        message if validation fails or character already
        exists.
        """
        # Get name, ep and fp fields
        try:
            name = self.name_frame.name_field.get_validated()
            sfe_map = self.sfe_frame.retrieve_sfe_map()
            ep_fp_result = self.ep_fp_frame.get_ep_fp()

        except FieldValidationError as error:
            self.character_page.messages.write_message(error.message)
            return

        # Add exceptional sfe values to map using specified key
        sfe_map = copy_value_to_keys(sfe_map, mgc.CHEST, mgc.RCOLLARBONE,
                                     mgc.LCOLLARBONE)
        sfe_map = insert_torso_back_armour(sfe_map)

        ep_fp_result[mgc.NAME] = name
        ep_fp_result[mgc.SFE] = sfe_map

        # Add new character. Addition fails if character already exists.
        success, msg = self.character_page.characters.add_character(
            name, ep_fp_result)

        if not success:
            msg = ALREADY_ADDED.format(name)

        else:
            msg = SUCCESS

            # Autosave current characters in memory
            save_characters(self.character_page.characters.character_maps)

        self.character_page.messages.write_message(msg)


class NameFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains
    name field with label.
    """
    def __init__(self, character_panel):
        ttk.LabelFrame.__init__(self, character_panel, text=NEV_LABEL)

        self.name_field = CharacterValueField(self, validate_string)
        organize_rows_to_left([self.name_field], NAME_COLUMN)

    def reset_frame(self):
        """
        Resets all the child widgets of the frame.
        """
        on_all_children('reset_fld', self)


class EpFpFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains
    ep and fp fields with labels.
    """
    def __init__(self, character_panel):
        ttk.LabelFrame.__init__(self, character_panel, text=EP_FRAME_TITLE)

        self.ep_field = CharacterValueField(self, validate_integer,
                                            width=3, name=mgc.MAX_EP)
        self.akt_ep_field = CharacterValueField(self, validate_integer,
                                                width=3, name=mgc.ACT_EP)
        self.ep_field.value.trace('w', self._set_actual)

        self.fp_field = CharacterValueField(self, validate_integer,
                                            width=3, name=mgc.MAX_FP)
        self.akt_fp_field = CharacterValueField(self, validate_integer,
                                                width=3, name=mgc.ACT_FP)
        self.fp_field.value.trace('w', self._set_actual)

        self.is_not_living_state = IntVar()
        self.is_not_living_state.set(0)
        self.is_not_living = Checkbutton(self, text='Elettelen',
                                         variable=self.is_not_living_state)

        self.is_not_living_state.trace('w', self._set_living_state)

        ep_last_column = place_max_act_fields(
            self, self.ep_field, self.akt_ep_field, label_text=EP_LABEL)

        place_max_act_fields(
            self, self.fp_field, self.akt_fp_field, label_text=FP_LABEL, start_row=1)

        self.is_not_living.grid(column=ep_last_column, row=0)

    def get_ep_fp(self):
        ep_fp_dict = {}
        fields = collect_children_type_of(self, 'Entry')

        for field in fields:
            if field.cget('state') == 'normal' and hasattr(field, 'name'):
                key = field.name

                try:
                    value = field.get_validated()
                    ep_fp_dict[key] = value

                except FieldValidationError:
                    raise

        return ep_fp_dict

    def reset_frame(self):
        """
        Resets all the child widgets of the frame.
        """
        on_all_children('reset_fld', self)

    def _set_living_state(self, *_args):
        if self.is_not_living_state.get():
            self.fp_field.disable()
            self.akt_fp_field.disable()

        else:
            self.fp_field.enable()
            self.akt_fp_field.enable()

    def _set_actual(self, name, _i, _mode):
        """
        Sets the actual FP and EP values based on the maximum.
        """
        if name == 'max_ep':
            if self.ep_field.value:
                self.akt_ep_field.value.set(self.ep_field.value.get())

        elif name == 'max_fp':
            if self.fp_field.value:
                self.akt_fp_field.value.set(self.fp_field.value.get())


class SfeFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains the
    main sfe box and all body-part sfe boxes.
    """
    def __init__(self, character_panel):
        ttk.LabelFrame.__init__(self, character_panel, text=SFE_FRAME_TITLE)
        self.sfe = {}

        Label(self, text=SFE_SHORTCUT_LABEL).grid(row=0,
                                                  column=SFE_FIELDS_COLUMN)
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe_field.grid(row=0, column=SFE_FIELDS_COLUMN + 1)

        self.fej_sfe = SfePartFrame(self, SFE_FEJ_PARTS, self.sfe_field.value,
                                    self.sfe,
                                    main_text=SFE_FEJ_LABEL)
        self.torzs_sfe = SfePartFrame(self, SFE_TORZS_PARTS, self.sfe_field.value,
                                      self.sfe,
                                      main_text=SFE_TORZS_LABEL)

        self.kar_sfe = SfePartFrame(self, SFE_KAR_PARTS, self.sfe_field.value,
                                    self.sfe,
                                    main_text=SFE_KAR_LABEL,
                                    is_limb=True)
        self.lab_sfe = SfePartFrame(self, SFE_LAB_PARTS, self.sfe_field.value,
                                    self.sfe,
                                    main_text=SFE_LAB_LABEL,
                                    is_limb=True)

        place_next_in_columns([self.fej_sfe,
                               self.torzs_sfe,
                               self.kar_sfe,
                               self.lab_sfe],
                              1, SFE_FIELDS_COLUMN, PART_SFE_COLUMN_SPAN)

    def reset_frame(self):
        """
        Resets all the child widgets of the frame.

        Only resets one field, but that triggers the
        resetting of all other fields.
        """
        self.sfe_field.reset_fld()

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


class SfePartFrame(ttk.LabelFrame):
    """
    Frame child type of main sfe frame. E.g. Torso or Head frame.
    """
    def __init__(self, sfe_main_frame, body_parts, shortcut_value, sfe_dict,
                 main_text=None, shortcut_text=SFE_SHORTCUT_LABEL, is_limb=False):
        ttk.LabelFrame.__init__(self, sfe_main_frame, text=main_text)

        self.body_parts = body_parts

        if is_limb:
            self._sort_body_parts(body_parts)

        # Sfe value shortcut that sets all other sfe values
        self.master_sfe = shortcut_value
        self.master_sfe.trace('w', self._follow_master)

        Label(self, text=shortcut_text).grid(row=0, column=0, sticky=W)

        # Sfe shortcut that sets all sfe values listed in body_parts
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe_field.grid(row=0, column=1, sticky=W)
        self.sfe_field.value.trace('w', self._follow_total)

        # Dict attribute holding validated sfe values
        self.sfe_map = sfe_dict

        if is_limb:
            self._place_sfe_fields_limbs(body_parts)

        else:
            self._place_sfe_fields(body_parts)

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
        self.body_parts = result

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

    def _place_sfe_fields_limbs(self, fields):
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

            # Add only one label though
            label = Label(self, text=label_text)
            label.grid(row=row, column=column, sticky=W)

            # Place right and left limb field
            for sfe_field in [right_part, left_part]:
                sfe_field_value = CharacterValueField(
                    self, validate_integer, width=2)

                # Right (jobb) limbs are left aligned,
                # left (bal) limbs are right aligned
                if sfe_field == right_part:
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
            if key in self.body_parts:
                total = self.sfe_field.value.get()
                value.value.set(total)
