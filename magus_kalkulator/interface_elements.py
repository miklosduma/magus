"""
Generic, reusable interface elements and constants.
"""

from tkinter import Entry, StringVar, W, N, ttk, Label
from magus_kalkulator.validate import FieldValidationError, validate_integer

FIELD_WIDTH = 10
FIELD_COLOR = 'white'
FIELD_COLOR_ERROR = 'red'


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
    def __init__(self, master, validate_fun, width=FIELD_WIDTH):
        """
        Initialise input field.
         - validate_fun:
            A function used to validate the field's input value.
        """
        # Varible for entered value
        self.value = StringVar(master)
        self.value.set('')
        self.value.trace('w', self._follow_changes)
        self.validator = validate_fun

        # Entry field
        Entry.__init__(self, master, textvariable=self.value,
                       width=width)

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

        print(self.value.get())

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


class SfePartFrame(ttk.LabelFrame):
    """
    Frame child type of main sfe frame. E.g. Torso or Head frame.
    """
    def __init__(self, master, main_text, shortcut_text, body_parts):
        ttk.LabelFrame.__init__(self, master, text=main_text)
        self.master = master
        self.body_parts = body_parts

        # Sfe value shortcut that sets all other sfe values
        self.master_sfe = self.master.sfe_field.value
        self.master_sfe.trace('w', self._follow_master)

        Label(self, text=shortcut_text).grid(row=0, column=0, sticky=W)

        # Sfe shortcut that sets all sfe values listed in body_parts
        self.sfe_field = CharacterValueField(self, validate_integer, width=2)
        self.sfe_field.grid(row=0, column=1, sticky=W)
        self.sfe_field.value.trace('w', self._follow_total)

        # Dict attribute holding validated sfe values
        self.sfe_map = self.master.sfe

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
