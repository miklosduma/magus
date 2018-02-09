"""
Entry point of scripts. Use python[3] magus_kalkulator to fire up interface.
"""
from tkinter import Tk, mainloop

from magus_kalkulator.interface import MagusGUI


def fire_up_interface():
    """
    Starts the GUI when called from
    the command-line.
    """
    root = Tk()
    MagusGUI(root)
    mainloop()


# Fire up interface.
fire_up_interface()
