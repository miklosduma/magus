from tkinter import (ttk, Text, END, DISABLED, NORMAL, N, NE)

from karakterek import Karakterek
from interface_sebzes import SebzesPage
from interface_karakterek import KarakterPage


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WINDOW_DIMENSIONS = '800x800'
WINDOW_TEXT = 'Magus kalkulator'

TAB_PANEL_WIDTH = int(WINDOW_WIDTH/2)

TEXT_START = 'Udv kockak!'

KARAKTER_PAGE_TITLE = 'Karakterek'
SEBZES_PAGE_TITLE = 'Sebzes'

MESSAGE_BOX_COLOUR = 'azure'

TABS_COLUMN = 0
TABS_COLUMN_SPAN = 9
TABS_ROW = 0
TABS_ROW_SPAN = 5

MESSAGES_COLUMN = 9
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

        """
        style = ttk.Style()

        style.theme_create("yummy", parent="alt", settings={
        "TLabelframe": {"configure": {"background": "red"}}})

        style.theme_use("yummy")
        """

        # Create multiple tabs on main page, making characters
        # accessible to each
        self.messages = GuiMessage(self.master)
        self.tabs = MyTabs(self.master, self)
        self.tabs.grid(column=TABS_COLUMN, columnspan=TABS_COLUMN_SPAN,
                       row=TABS_ROW, rowspan=TABS_ROW_SPAN, sticky=N)
        self.messages.grid(column=MESSAGES_COLUMN,
                           columnspan=MESSAGES_COLUMNSPAN, sticky=N,
                           row=MESSAGES_ROW, rowspan=MESSAGES_ROWSPAN)


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
        ttk.Notebook.__init__(self, master, width=TAB_PANEL_WIDTH)
        self.karakterek = master_gui.karakterek
        self.messages = master_gui.messages
        self.master = master

        # Initialize tabs
        self.karakter_page = KarakterPage(self, master_gui, TAB_PANEL_WIDTH)
        self.sebzes_page = SebzesPage(self, master_gui, TAB_PANEL_WIDTH)
        self.add(self.karakter_page, text=KARAKTER_PAGE_TITLE)
        self.add(self.sebzes_page, text=SEBZES_PAGE_TITLE)


class GuiMessage(Text):
    def __init__(self, master):
        Text.__init__(self, master, bg=MESSAGE_BOX_COLOUR,
                      width=TAB_PANEL_WIDTH)
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
        print(self.winfo_width())
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