"""
Main interface window and top-level components, such as the messages panel
and the tabs frame.


Use style to customise interface.

style = ttk.Style()
style.theme_create("yummy", parent="alt", settings={
    "TLabelframe": {"configure": {"background": "red"}}})

style.theme_use("yummy")
"""

from tkinter import ttk, Text, END, DISABLED, NORMAL, N, mainloop, Tk

from magus_kalkulator.karakterek import Characters
from magus_kalkulator.interface_sebzes import SebzesPage
from magus_kalkulator.interface_karakterek import KarakterPage
from magus_kalkulator.interface_manage import ManagementPage
from magus_kalkulator.interface_elements import on_all_children


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


def fire_up_interface():
    """
    Starts the GUI when called from
    the command-line.
    """
    root = Tk()
    MagusGUI(root)
    mainloop()


class MagusGUI:
    """
    Base class for the magus calculator GUI.
    On init creates an instance of the characters
    object which it will make available for all
    elements of the GUI.
    """
    def __init__(self, root):
        """
        Initialize magus GUI. It's master is
        the TK root element.
        """
        # Initialize characters object
        self.characters = Characters()

        # Format main GUI window
        root.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        root.maxsize(WINDOW_WIDTH, WINDOW_HEIGHT)
        root.geometry(WINDOW_DIMENSIONS)
        root.title(WINDOW_TEXT)

        messages = GuiMessage(root)
        messages.grid(column=MESSAGES_COLUMN,
                      columnspan=MESSAGES_COLUMNSPAN, sticky=N,
                      row=MESSAGES_ROW, rowspan=MESSAGES_ROWSPAN)

        # Create multiple tabs on main page, making characters
        # accessible to each
        tabs = MyTabs(root, self.characters, messages)
        tabs.grid(column=TABS_COLUMN, columnspan=TABS_COLUMN_SPAN,
                  row=TABS_ROW, rowspan=TABS_ROW_SPAN, sticky=N)


class MyTabs(ttk.Notebook):
    """
    Base class for tabs frame. It can support
    one or more tabs added to it as separate pages.
    """
    def __init__(self, magus_gui, characters, messages):
        """
        Initialise tabs frame. It gets the characters
        object from the top level and hands them down to
        the slave pages.
        """
        ttk.Notebook.__init__(self, magus_gui, width=TAB_PANEL_WIDTH)

        # Initialize tabs
        karakter_page = KarakterPage(self, characters, messages,
                                     TAB_PANEL_WIDTH)
        sebzes_page = SebzesPage(self, characters, messages,
                                 TAB_PANEL_WIDTH)
        manage_page = ManagementPage(self, characters, messages,
                                     TAB_PANEL_WIDTH)

        self.add(karakter_page, text=KARAKTER_PAGE_TITLE)
        self.add(sebzes_page, text=SEBZES_PAGE_TITLE)
        self.add(manage_page, text="Kezeles")
        self.bind("<<NotebookTabChanged>>", self.on_change)

    def on_change(self, _event):
        """
        Resets all tabs on changing tabs.
        """
        on_all_children('reset_page', self)


class GuiMessage(Text):
    """
    Class for the main message panel.
    """
    def __init__(self, magus_gui):
        """
        Initialise main message panel.

        Its master must be the root element.
        """
        Text.__init__(self, magus_gui, bg=MESSAGE_BOX_COLOUR,
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
