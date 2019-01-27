"""
GUI page for adding new characters.
"""
from tkinter import W, E, VERTICAL, ttk, IntVar

from magus_kalkulator.validate import (validate_integer, validate_string,
                                       FieldValidationError)
from magus_kalkulator.interface_elements import (CharacterValueField,
                                                 ChooseCharacterFrame,
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
ADD_BUTTON = 'Ok'
GET_BUTTON = 'Karakterek'

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


def place_fields_separator(frame, *fields, **kwargs):
    """
    Appends frame element with new fields. The fields
    are placed next to each other, with a separator
    placed between them.

    If no other separator is specified, the symbol
    '/' is used.
    """
    start_column = kwargs.get('start_column', 0)
    start_row = kwargs.get('start_row', 0)
    separator = kwargs.get('separator', '/')

    if 'label_text' in kwargs:
        ttk.Label(frame, text=kwargs.get('label_text')).grid(
            column=start_column, row=start_row)
        start_column += 1

    for field in fields:
        field.grid(column=start_column, row=start_row)
        start_column += 1

        if field != fields[-1]:
            ttk.Label(frame, text=separator).grid(
                column=start_column, row=start_row)
            start_column += 1

    return start_column


def get_child_values(parent, ch_type,
                     val_dict=None,
                     get_method='get'):
    """
    Collects the values of all children of 'parent'
    who are of the specified type.

    For example, all Entry children of a frame.

    The function either builds, or updates a dictionary,
    where the child element's name attribute is used as
    a key, and its value as the value.

    The function only collects values from elements that
    are in active state (not disabled) and have the 'name'
    attribute.
        - parent:
            The parent tkinter element.
        - ch_type:
            The type of children to be collected.
        - val_dict (optional):
            The function may be called to extend/update
            an existing dictionary.
        - get_method (optional):
            The method called on the element to retrieve
            it's value. By default, it's 'get'.
    """
    if not val_dict:
        val_dict = dict()

    children = collect_children_type_of(parent, ch_type)

    for child in children:
        if hasattr(child, 'state'):

            if 'disabled' not in child.state():

                key = child.name
                value = getattr(child, get_method)()
                val_dict[key] = value

    return val_dict


class KarakterPage(ttk.Frame):
    """
    Adding characters main page.
    """
    def __init__(self, tabs_master, characters, messages):

        self.messages = messages

        ttk.Frame.__init__(self, tabs_master)

        self.is_modify = IntVar()
        self.is_modify.trace('w', self._callback)
        self.modify_box = ttk.Checkbutton(self,
                                          variable=self.is_modify,
                                          text='Modosit')
        self.modify_box.grid(row=0, sticky=W, pady=4)

        self.panels = KarakterPanels(self, characters)
        self.panels.grid(column=0, row=1, columnspan=2)

        add_button = ttk.Button(self, text=ADD_BUTTON)
        add_button.bind('<Button-1>', self.panels.add_character)
        add_button.grid(column=0, row=2, padx=8, pady=4, sticky=W)

        get_button = ttk.Button(self, text=GET_BUTTON)
        get_button.bind('<Button-1>', self.panels.get_characters)
        get_button.grid(column=0, row=2, pady=4, padx=50, sticky=W)

    def _callback(self, *_event):
        self.panels.change_mode(self.is_modify.get())

    def reset_page(self):
        """
        Resets all the child widgets of the page.
        """
        if self.is_modify.get():
            self.is_modify.set(0)
        self.panels.reset_panel()


class KarakterPanels(ttk.PanedWindow):
    """
    Main panel of characters main page.
    """
    def __init__(self, character_page, characters, orient=VERTICAL):
        ttk.PanedWindow.__init__(self, character_page, orient=orient)
        self.character_page = character_page
        self.characters = characters

        self.name_frame = NameFrame(self)
        self.add(self.name_frame)

        self.name_dropdown = ChooseCharacterFrame(self, self.characters)
        self.name_dropdown.character_menu.bind(
            '<<ComboboxSelected>>', self._callback)

        self.ep_fp_frame = EpFpFrame(self)
        self.add(self.ep_fp_frame)

        self.sfe_frame = SfeFrame(self)
        self.add(self.sfe_frame)

    def _callback(self, *_event):
        selected_character = self.name_dropdown.character_menu.get()
        if selected_character:
            character_values = self.characters.get_character(selected_character)

            for frame in self.ep_fp_frame, self.sfe_frame:
                fields = collect_children_type_of(frame, 'TEntry', recursive=True)
                for field in fields:
                    try:
                        field_name = field.name
                        if field_name in character_values:
                            field.value.set(character_values[field_name])

                        elif field_name in character_values['sfe']:
                            field.value.set(character_values['sfe'][field_name])

                    except AttributeError:
                        pass

    def change_mode(self, is_modify):

        if is_modify:
            self.insert(self.name_frame, self.name_dropdown)
            self.forget(self.name_frame)

        else:
            self.insert(self.name_dropdown, self.name_frame)
            self.forget(self.name_dropdown)
            self.character_page.reset_page()

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
            list(self.characters.get_character_names())

        if not all_characters:
            self.character_page.messages.write_message(NO_CHARACTERS)

        else:
            self.character_page.messages.write_characters(self.characters, all_characters)

    def add_character(self, *_args):
        """
        Function executed on clicking Add button.

        Either adds a new character or returns error
        message if validation fails or character already
        exists.
        """
        is_modify = self.character_page.is_modify.get()
        if is_modify:
            name = self.name_dropdown.character_menu.get()
            print(name)

            if not name:
                self.character_page.messages.write_message('Valassz egy karaktert!')
                return

        else:
            try:
                name = self.name_frame.name_field.get_validated()

            except FieldValidationError as error:
                self.character_page.messages.write_message(error.message)
                return

        # Get name, ep and fp fields
        try:
            sfe_map = self.sfe_frame.retrieve_sfe_map()
            ep_fp_result = get_child_values(self.ep_fp_frame, 'TEntry',
                                            get_method='get_validated')

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
        success, msg = self.characters.add_character(
            name, ep_fp_result, is_modify=is_modify)

        if not success:
            msg = ALREADY_ADDED.format(name)

        else:
            msg = SUCCESS

            # Autosave current characters in memory
            save_characters(self.characters.character_maps)
            self.character_page.reset_page()

        self.character_page.messages.write_message(msg)


class NameFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains
    name field with label.
    """
    def __init__(self, character_panel):
        ttk.LabelFrame.__init__(self, character_panel, text=NEV_LABEL)

        self.name_field = CharacterValueField(self, validate_string)
        self.name_field.grid()

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
                                                width=3, name=mgc.ACT_EP,
                                                to_trace=self.ep_field.value)

        self.fp_field = CharacterValueField(self, validate_integer,
                                            width=3, name=mgc.MAX_FP)
        self.akt_fp_field = CharacterValueField(self, validate_integer,
                                                width=3, name=mgc.ACT_FP,
                                                to_trace=self.fp_field.value)

        self.is_not_living_state = IntVar()
        self.is_not_living_state.set(0)
        self.is_not_living = ttk.Checkbutton(self, text='Elettelen',
                                             variable=self.is_not_living_state)

        self.is_not_living_state.trace('w', self._set_living_state)

        ep_last_column = place_fields_separator(
            self, self.ep_field, self.akt_ep_field, label_text=EP_LABEL)

        place_fields_separator(
            self, self.fp_field, self.akt_fp_field,
            label_text=FP_LABEL, start_row=1)

        self.is_not_living.grid(column=ep_last_column, row=0)

    def reset_frame(self):
        """
        Resets all the child widgets of the frame.
        """
        on_all_children('reset_fld', self)
        self.is_not_living_state.set(0)

    def _set_living_state(self, *_args):
        if self.is_not_living_state.get():
            self.fp_field.disable()
            self.akt_fp_field.disable()

        else:
            self.fp_field.enable()
            self.akt_fp_field.enable()


class SfeFrame(ttk.LabelFrame):
    """
    Part of characters panel. Contains the
    main sfe box and all body-part sfe boxes.
    """
    def __init__(self, character_panel):
        ttk.LabelFrame.__init__(self, character_panel, text=SFE_FRAME_TITLE)
        self.sfe = {}

        ttk.Label(self, text=SFE_SHORTCUT_LABEL).grid(
            row=0, column=SFE_FIELDS_COLUMN)
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe_field.grid(row=0, column=SFE_FIELDS_COLUMN + 1)

        self.fej_sfe = SfePartFrame(self, SFE_FEJ_PARTS,
                                    self.sfe_field.value,
                                    main_text=SFE_FEJ_LABEL)
        self.torzs_sfe = SfePartFrame(self, SFE_TORZS_PARTS,
                                      self.sfe_field.value,
                                      main_text=SFE_TORZS_LABEL)

        self.kar_sfe = SfePartFrame(self, SFE_KAR_PARTS,
                                    self.sfe_field.value,
                                    main_text=SFE_KAR_LABEL,
                                    is_limb=True)
        self.lab_sfe = SfePartFrame(self, SFE_LAB_PARTS,
                                    self.sfe_field.value,
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

        for key, value in self.sfe.items():
            value = value.get_validated()
            return_map[key] = value
        return return_map


class SfePartFrame(ttk.LabelFrame):
    """
    Frame child type of main sfe frame. E.g. Torso or Head frame.
    """
    def __init__(self, sfe_main_frame, body_parts, shortcut_value, **kwargs):
        """
        Create SFE part frame instance.
        """
        ttk.LabelFrame.__init__(self, sfe_main_frame,
                                text=kwargs.get('main_text', None))

        # Sfe value shortcut that sets all other sfe values
        self.master_sfe = shortcut_value
        self.sfe_main_frame = sfe_main_frame

        ttk.Label(self,
                  text=kwargs.get(
                      'shortcut_text', SFE_SHORTCUT_LABEL)).grid(
            row=0, column=0, sticky=W)

        # Sfe shortcut that sets all sfe values listed in body_parts
        self.sfe_field = CharacterValueField(self, validate_integer, width=2,
                                             to_trace=self.master_sfe)
        self.sfe_field.grid(row=0, column=1, sticky=W)

        if 'is_limb' in kwargs:
            self._place_sfe_fields_limbs(body_parts)

        else:
            self._place_sfe_fields(body_parts)

    def _place_sfe_fields(self, fields):
        """
        Function to place multiple connected fields assigning
        each a label.
        """
        column = 0
        row = 1

        for field in fields:
            # Place label, it takes its name from the field
            label = ttk.Label(self, text=field)
            label.grid(row=row, column=column, sticky=W)

            # Place field next to label
            sfe_field = CharacterValueField(self, validate_integer, width=2,
                                            to_trace=self.sfe_field.value,
                                            name=field)
            sfe_field.grid(row=row, column=column + 1, sticky=W)

            # Add sfe field to sfe map. Sfe field stores the value
            # of the entry field
            self.sfe_main_frame.sfe[field] = sfe_field

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
        jobb_bal = ttk.Label(self, text=RIGHT_LEFT_LABEL)
        jobb_bal.grid(row=row, column=column + 1)

        # Place everything below Jobb/Bal label
        row += 1

        for field in fields:
            label_text, right_part, left_part = field

            # Add only one label though
            label = ttk.Label(self, text=label_text)
            label.grid(row=row, column=column, sticky=W)

            # Place right and left limb field
            for sfe_field in [right_part, left_part]:
                sfe_field_value = CharacterValueField(
                    self, validate_integer,
                    width=2, to_trace=self.sfe_field.value,
                    name=sfe_field)

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
                self.sfe_main_frame.sfe[sfe_field] = sfe_field_value

            # Next label/field will go into next row
            row += 1
