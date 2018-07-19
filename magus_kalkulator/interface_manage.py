"""
Character management. E.g deleting/updating characters.
"""

from tkinter import ttk, VERTICAL, Button, filedialog

from magus_kalkulator.interface_elements import organize_rows_to_left, \
    ChooseCharacterFrame, on_all_children, save_characters, load_characters


class ManagementPage(ttk.Frame):
    """
    Adding characters main page.
    """
    def __init__(self, master, master_gui, width):
        """
        Initialise management page.
        """
        self.master = master
        self.karakterek = master_gui.karakterek
        self.messages = master_gui.messages
        ttk.Frame.__init__(self, master, width=width)
        self.main_panel = CharacterPanel(self, width)
        self.del_button = Button(self, text='Torles')
        self.del_button.bind('<Button-1>', self.del_character)

        self.load_button = Button(self, text='Load')
        self.load_button.bind('<Button-1>', self.load_char)

        # Place elements on grid
        organize_rows_to_left([self.main_panel, self.del_button,
                               self.load_button], 0)

    def load_char(self, *_args):
        """
        Replaces the characters storage with the content of a file.
        Cleans all currently stored characters.
        """

        # Propmts the user to pick a backup file in the saves directory.
        file_path = filedialog.askopenfilename(initialdir='saves')
        if not file_path:
            return


        # The characters are saved as json, load them.
        saved_chars = load_characters(file_path)

        if not saved_chars:
            return

        # Get rid of all currently saved characters.
        self.karakterek.delete_all_characters()

        # Load each saved character into memory.
        for char_name, char_values in saved_chars.items():
            self.karakterek.add_karakter(char_name,
                                         char_values['max_ep'],
                                         char_values['sfe'],
                                         max_fp=char_values['max_fp'])

    def del_character(self, *_args):
        """
        Deletes the selected character.
        """
        success, selected = self.main_panel.choose_frame.get_selected()

        if success:
            self.karakterek.delete_karakter(selected)
            self.main_panel.choose_frame.variable.set('')

            # Update characters kept in memory
            save_characters(self.karakterek.karakterek)

        else:
            self.messages.write_message(selected)

    def reset_page(self):
        """
        Resets all child widgets of the frame.
        """
        on_all_children('reset_panel', self)


class CharacterPanel(ttk.PanedWindow):
    """
    Main panel of damage page.
    """
    def __init__(self, master, width, orient=VERTICAL):
        """
        Initialise main panel.
        """
        ttk.PanedWindow.__init__(self, master, width=width, orient=orient)
        self.master = master

        self.choose_frame = ChooseCharacterFrame(self, self.master.karakterek)
        organize_rows_to_left([self.choose_frame], 0)

    def reset_panel(self):
        """
        Resets all child widgets of this panel.
        """
        on_all_children('reset_frame', self)
