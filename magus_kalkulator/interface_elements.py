"""
Generic, reusable interface elements and constants.
"""

import os
import json

from tkinter import StringVar, W, N, ttk
from magus_kalkulator.validate import FieldValidationError

FIELD_WIDTH = 10
FIELD_COLOR = 'white'
SELECT_CHARACTER = 'Valaszz karaktert'
NO_CHARACTER = 'Valassz karaktert!'
MSG_TAB = 4


def format_list_msg(list_value):
    """
    Formats a key/value pair where the value
    is a list.

    Each list element is placed on a new line, they are
    all indented by a specified tab.
    """
    separator = '\n'
    for _i in range(0, MSG_TAB):
        separator += ' '

    return '{}{}'.format(separator, separator.join(list_value))


def get_relative_dir(target_path):
    """
    Returns the full - relative - path to
    'target_path'.
    """
    full_path, _rest = os.path.dirname(__file__).rsplit('/', 1)
    return os.path.join(full_path, target_path)


def organize_rows_to_left(list_of_elements, column, start_row=0):
    """
    Places all elements in the list under each other
    in the specified column.

    They are all left-aligned.
    """
    for element in list_of_elements:
        element.grid(column=column, row=start_row, sticky=W)
        start_row += 1

    return start_row


def on_all_children(method, parent):
    """
    Calls the specified method on all child widgets
    of parent if the widgets have that method.
    """
    for child in parent.winfo_children():
        if hasattr(child, method):
            getattr(child, method)()


def save_characters(characters, filename='saves/autosave.json'):
    """
    Retrieves all stored characters and saves them
    to file.
    """
    with open(filename, 'w') as backup:
        if characters:
            backup.write(json.dumps(characters, indent=4))

        else:
            backup.write('')


def load_characters(path_to_backup):
    """
    Characters are saved in a json file.
    Read and return the saved content
    as a Python dict.
    """
    with open(path_to_backup, 'r') as content:
        try:
            return json.loads(content.read())
        except json.JSONDecodeError:
            pass


def collect_children_type_of(parent, ch_type, recursive=False, collected=None):
    """
    Collect specific children of the tkinter
    parent element.
        - parent:
            The tkinter parent element.
            (E.g. a Frame).
        - ch_type:
            The type of children to be collected.
            (E.g. Entry).
    """
    if not collected:
        collected = list()

    for child in parent.winfo_children():

        if child.winfo_class() == ch_type:
            collected.append(child)

        if recursive:
            collected = collect_children_type_of(child, ch_type, recursive=True,
                                                 collected=collected)

    return collected


def place_next_in_columns(frames, row, column, columnspan,
                          padx=0, pady=0):
    """
    Places the specified frame elements.
    """
    # Save value of column parameter
    start_column = column

    # Place all frame elements
    for frame in frames:
        frame.grid(row=row,
                   column=column,
                   columnspan=columnspan,
                   sticky=(N, W))

        # If column is the same as columnspan, next item is placed in new row
        if column == columnspan:
            column = start_column
            row += 1

        # Else place in next column
        else:
            column += columnspan


class CharacterValueField(ttk.Entry):
    """
    Basic field type used to store character values.
    """
    def __init__(self, parent, validate_fun, **kwargs):
        """
        Initialise input field.
         - validate_fun:
            A function used to validate the field's input value.
        """
        # Variable for entered value
        if 'name' in kwargs:
            self.name = kwargs.get('name')
            self.value = StringVar(parent, name=self.name)
        else:
            self.value = StringVar(parent)
        self.value.set('')
        self.value.trace('w', self._follow_changes)
        self.validator = validate_fun

        if 'to_trace' in kwargs:
            self.reference = kwargs.get('to_trace')
            self.reference.trace('w', self._follow_ref_val)

        # Entry field
        ttk.Entry.__init__(self, parent,
                           textvariable=self.value,
                           width=kwargs.get('width', FIELD_WIDTH))

    def _follow_ref_val(self, *_args):
        """
        If a master - or reference - value is specified
        for the field, it will update its value on changes
        to the master field.
        """
        self.value.set(self.reference.get())

    def _follow_changes(self, *_args):
        """
        Traces changes to the input value
        of the field.
        """
        if 'invalid' in self.state():
            self.state(['!invalid'])

    def enable(self):
        """
        Enables the field. I.e. it's value
        can be set.
        """
        self.state(['!disabled'])

    def disable(self):
        """
        Disables the field. It's value cannot
        be set or edited.
        """
        self.state(['disabled'])

    def get_validated(self, **kwargs):
        """
        Calls assigned validator function on the
        value of the field.

        If validation fails, turns the field to red.
        """
        try:
            value = self.validator(self.value.get(), **kwargs)
            return value

        except FieldValidationError:
            self.state(['invalid'])
            raise

    def reset_fld(self):
        """
        Cleans the field's value by setting
        it to an empty string.
        """
        self.value.set('')


class Spinbox(ttk.Entry):
    """
    ttk.Spinbox missing from pre-Python 3.7 versions.
    """

    def __init__(self, master=None, **kw):
        kw['state'] = 'readonly'
        ttk.Entry.__init__(self, master, 'ttk::spinbox', **kw)
        self.config(width=2)

    def set(self, value):
        self.tk.call(self._w, "set", value)

    def enable(self):
        """
        Enables the field. I.e. it's value
        can be set.
        """
        self.state(['!disabled'])


class CharacterDropDown(ttk.Combobox):
    """
    Read-only drop-down menu instance that calculates its width
    based on values.
    """
    def __init__(self, master, **kwargs):
        """
        Initialise ttk Combobox with read-only state.
        """
        kwargs['state'] = 'readonly'
        ttk.Combobox.__init__(self, master, **kwargs)
        if 'values' in kwargs:
            self.width_match_longest(kwargs['values'])

    def width_match_longest(self, values):
        """
        Width of menu list must match longest menu item.
        """
        lengths = [len(str(x)) for x in values if x]

        if lengths:
            self.config(width=max(lengths) + 2)

    def reset_drop_down(self):
        """
        Sets the drop-down to either the first element of values
        or to an empty string.
        """
        if self['values']:
            self.set(self['values'][0])

        else:
            self.set('')

    def enable(self):
        """
        Enables the field. I.e. it's value
        can be set.
        """
        self.state(['!disabled'])

    def disable(self):
        """
        Disables the field. It's value cannot
        be set or edited.
        """
        self.state(['disabled'])


class ChooseCharacterFrame(ttk.LabelFrame):
    """
    Frame comprising character-selection drop-down.
    """
    def __init__(self, master, characters):
        """
        Initialise character-selection frame.
        """
        self.master = master
        ttk.LabelFrame.__init__(self, master, text=SELECT_CHARACTER)
        self.characters = characters
        self.character_menu = CharacterDropDown(self, values=[''])
        self.character_menu.bind('<Button-1>', self._update)
        self.character_menu.grid()

    def get_selected(self):
        """
        Return latest value.
        """
        character = self.character_menu.get()

        if character:
            return True, character

        return False, NO_CHARACTER

    def _update(self, _event):
        """
        When clicking the drop-down, get the name of
        all characters currently in memory.
        """
        new_choices = self.characters.get_character_names()
        if new_choices:
            self.character_menu['values'] = list(new_choices)
            self.character_menu.width_match_longest(new_choices)

        else:
            self.character_menu['values'] = ['']

    def reset_frame(self):
        """
        Cleans the field's value by setting
        it to an empty string.
        """
        self.character_menu.set('')
