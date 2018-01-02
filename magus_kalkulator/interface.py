from tkinter import (Tk, mainloop, ttk, Text, END, DISABLED, NORMAL, N, W)

from karakterek import Karakterek
from interface_sebzes import SebzesPage
from interface_karakterek import KarakterPage


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 600
WINDOW_DIMENSIONS = '960x600'
WINDOW_TEXT = 'Magus kalkulator'

TEXT_START = 'Udv kockak!'

KARAKTER_PAGE_TITLE = 'Karakterek'
SEBZES_PAGE_TITLE = 'Sebzes'

MESSAGE_BOX_COLOUR = 'azure'

TABS_COLUMN = 0
TABS_COLUMN_SPAN = 4
TABS_ROW = 0
TABS_ROW_SPAN = 5

MESSAGES_COLUMN = 4
MESSAGES_COLUMNSPAN = TABS_COLUMN_SPAN
MESSAGES_ROW = TABS_ROW
MESSAGES_ROWSPAN = TABS_ROW_SPAN

START_INDEX = 1.0


class MagusGUI:
    """
    Base class for the magus calculator GUI.
    On init creates an instance of the characters
    object which it will make available for all
    elements of the GUI.
    """
    def __init__(self, master):
        """
        Initialize magus GUI. It's master is
        the TK root element.
        """
        self.master = master

        # Initialize characters object
        self.karakterek = Karakterek()

        # Format main GUI window
        master.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        master.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        master.geometry(WINDOW_DIMENSIONS)
        master.title(WINDOW_TEXT)

        # Create multiple tabs on main page, making characters
        # accessible to each
        self.messages = GuiMessage(self.master)
        self.tabs = MyTabs(self.master, self)
        self.tabs.grid(column=TABS_COLUMN, columnspan=TABS_COLUMN_SPAN,
                       row=TABS_ROW, rowspan=TABS_ROW_SPAN, sticky=N)
        self.messages.grid(column=MESSAGES_COLUMN,
                           columnspan=MESSAGES_COLUMNSPAN, sticky=N,
                           row=MESSAGES_ROW, rowspan=MESSAGES_ROWSPAN)

    def organize_rows_to_left(self, list_of_elements, column, start_row=0):
        """
        Places all elements in the list under each other
        in the specified column.

        They are all left-aligned.
        """
        for element in list_of_elements:
            element.grid(column=column, row=start_row, sticky=W)
            start_row += 1

        return start_row


class MyTabs(ttk.Notebook):
    """
    Base class for tabs frame. It can support
    one or more tabs added to it as separate pages.
    """
    def __init__(self, master, master_gui):
        """
        Initialise tabs frame. It gets the characters
        object from the top level and hands them down to
        the slave pages.
        """
        ttk.Notebook.__init__(self, master)
        self.karakterek = master_gui.karakterek
        self.messages = master_gui.messages
        self.master = master

        # Initialize tabs
        self.karakter_page = KarakterPage(self, master_gui)
        self.sebzes_page = SebzesPage(self, master_gui)
        self.add(self.karakter_page, text=KARAKTER_PAGE_TITLE)
        self.add(self.sebzes_page, text=SEBZES_PAGE_TITLE)


class GuiMessage(Text):
    def __init__(self, master):
        Text.__init__(self, master, bg=MESSAGE_BOX_COLOUR)
        self.insert(END, TEXT_START)
        self._set_state(DISABLED)

    def _set_state(self, state):
        """
        Sets the state of the text box and saves the
        state into the state attribute.
        Possible states:
            - NORMAL (editable)
            - DISABLED (read-only)
        """
        self.config(state=state)
        self.state = state

    def delete_message(self):
        """
        Deletes the current content
        of the text box.
        """
        if self.state == DISABLED:
            self._set_state(NORMAL)

        self.delete(START_INDEX, END)

    def write_message(self, text):
        """
        Overrides the content of the text box
        with the provided text.
        """
        self.delete_message()
        self.insert(END, text)
        self._set_state(DISABLED)


def fire_up_interface():
    """
    Starts the GUI when called from
    the command-line.
    """
    root = Tk()
    MagusGUI(root)
    mainloop()


if __name__ == "__main__" :
    fire_up_interface()