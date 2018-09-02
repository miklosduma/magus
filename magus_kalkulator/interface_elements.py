"""
Generic, reusable interface elements and constants.
"""

import os
import json

from tkinter import Entry, StringVar, W, N, ttk, OptionMenu, DISABLED, NORMAL
from magus_kalkulator.validate import FieldValidationError

FIELD_WIDTH = 10
FIELD_COLOR = 'white'
FIELD_COLOR_ERROR = 'red'
SELECT_CHARACTER = 'Valaszz karaktert'
NO_CHARACTER = 'Valassz karaktert!'


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


def collect_children_type_of(parent, ch_type):
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
    collected = []

    for child in parent.winfo_children():
        if child.winfo_class() == ch_type:
            collected.append(child)

    return collected


def place_next_in_columns(frames, row, column, columnspan):
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


class CharacterValueField(Entry):
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
        Entry.__init__(self, parent, textvariable=self.value,
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
        # Get current background color of field.
        color = self.cget('bg')

        # It turns red on validation failures.
        # Any subsequent change must turn the color back
        # to the default color.
        if color == FIELD_COLOR_ERROR:
            self.config(bg=FIELD_COLOR)

    def enable(self):
        """
        Enables the field. I.e. it's value
        can be set.
        """
        self.config(state=NORMAL)
        self.value.set('')

    def disable(self):
        """
        Disables the field. It's value cannot
        be set or edited.
        """
        self.value.set('n/a')
        self.config(state=DISABLED)

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
            self.config(bg=FIELD_COLOR_ERROR)
            raise

    def reset_fld(self):
        """
        Cleans the field's value by setting
        it to an empty string.
        """
        self.value.set('')


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
        self.variable = StringVar()
        self.variable.set('')
        self.character_menu = OptionMenu(self, self.variable, *[''])
        self.character_menu.bind('<Button-1>', self._update)
        self.character_menu.config(width=10)
        self.character_menu.grid()

    def get_selected(self):
        """
        Return latest value.
        """
        character = self.variable.get()

        if character:
            return True, character

        return False, NO_CHARACTER

    def _width_match_longest(self, opt_list):
        """
        Width of menu list must match longest menu item.
        """

        if opt_list:
            lengths = [len(x) for x in opt_list]
            self.character_menu.config(width=max(lengths) + 2)

    def _update(self, _event):
        """
        When clicking the drop-down, get the name of
        all characters currently in memory.
        """
        menu = self.character_menu.children['menu']
        menu.delete(0, 'end')
        new_choices = self.characters.get_character_names()

        self._width_match_longest(new_choices)

        for value in new_choices:
            menu.add_command(label=value,
                             command=lambda v=value: self.variable.set(v))

    def reset_frame(self):
        """
        Cleans the field's value by setting
        it to an empty string.
        """
        self.variable.set('')
