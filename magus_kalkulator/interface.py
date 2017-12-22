from tkinter import (Tk, mainloop, ttk, Text, END, DISABLED, NORMAL, N)

from karakterek import Karakterek
from interface_sebzes import SebzesPage
from interface_karakterek import KarakterPage


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 600
WINDOW_DIMENSIONS = '960x600'
WINDOW_TEXT = 'Magus kalkulator'

TEXT_START = 'Udv kockak!'


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
        self.tabs = MyTabs(self.master, self.karakterek, self.messages)
        self.tabs.grid(column=0, columnspan=4, row=0, rowspan=5, sticky=N)
        self.messages.grid(column=4,columnspan=2)


class MyTabs(ttk.Notebook):
    """
    Base class for tabs frame. It can support
    one or more tabs added to it as separate pages.
    """
    def __init__(self, master, karakterek, messages):
        """
        Initialise tabs frame. It gets the characters
        object from the top level and hands them down to
        the slave pages.
        """
        ttk.Notebook.__init__(self, master)
        self.karakterek = karakterek
        self.messages = messages

        # Initialize tabs
        self.karakter_page = KarakterPage(self, self.karakterek, self.messages)
        self.sebzes_page = SebzesPage(self, self.karakterek, self.messages)
        self.add(self.karakter_page, text='Karakterek')
        self.add(self.sebzes_page, text='Sebzes')


class GuiMessage(Text):
    def __init__(self, master):
        Text.__init__(self, master, bg='azure')
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

        self.delete(1.0, END)

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