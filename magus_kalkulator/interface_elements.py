from tkinter import Entry, StringVar, W

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