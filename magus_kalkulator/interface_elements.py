from tkinter import Entry, StringVar, W, N
from validate import FieldValidationError

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
        frame.grid(row=row, column=column, columnspan=columnspan, sticky=(N, W))

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
