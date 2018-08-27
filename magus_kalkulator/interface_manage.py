"""
Character management. E.g deleting characters or saving/loading.
"""
from __future__ import print_function

import os
from tkinter import ttk, VERTICAL, Button, filedialog, messagebox

from magus_kalkulator.interface_elements import organize_rows_to_left, \
    ChooseCharacterFrame, on_all_children, save_characters, load_characters, \
    CharacterValueField

from magus_kalkulator.validate import validate_string, FieldValidationError


class ManagementPage(ttk.Frame):
    """
    Adding characters main page.
    """
    def __init__(self, master, characters, messages, width):
        """
        Initialise management page.
        """
        self.characters = characters
        self.messages = messages
        ttk.Frame.__init__(self, master, width=width)
        self.main_panel = CharacterPanel(self, characters, width)

        del_button = Button(self, text='Torles')
        del_button.bind('<Button-1>', self.del_character)

        load_button = Button(self, text='Load')
        load_button.bind('<Button-1>', self.load_char)

        self.save_text = CharacterValueField(self, validate_string)
        save_button = Button(self, text='Save')
        save_button.bind('<Button-1>', self.save_char)

        # Place elements on grid
        organize_rows_to_left([self.main_panel, del_button,
                               load_button, self.save_text,
                               save_button], 0)

    def save_char(self, *_args):
        """
        Saves all characters kept in memory.
        """
        try:
            file_name = '{}.json'.format(self.save_text.get_validated())

        except FieldValidationError as error:
            self.messages.write_message(error.message)
            return

        if not self.characters.character_maps:
            self.messages.write_message('Nincsenek mentheto karakterek.')
            return

        save_dir = os.path.join('saves', file_name)
        if os.path.exists(save_dir):
            if not messagebox.askyesno('Save', 'Overwrite existing file?'):
                return

        save_characters(self.characters.character_maps, filename=save_dir)
        self.messages.write_message('{} mentesre kerult.'.format(file_name))

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
        self.characters.delete_all_characters()

        # Load each saved character into memory.
        for char_name, char_values in saved_chars.items():
            self.characters.add_character(char_name, char_values)

    def del_character(self, *_args):
        """
        Deletes the selected character.
        """
        success, selected = self.main_panel.choose_frame.get_selected()

        if success:
            self.characters.delete_character(selected)
            self.main_panel.choose_frame.variable.set('')

            # Update characters kept in memory
            save_characters(self.characters.character_maps)

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
    def __init__(self, master, characters, width, orient=VERTICAL):
        """
        Initialise main panel.
        """
        ttk.PanedWindow.__init__(self, master, width=width, orient=orient)

        self.choose_frame = ChooseCharacterFrame(self, characters)
        organize_rows_to_left([self.choose_frame], 0)

    def reset_panel(self):
        """
        Resets all child widgets of this panel.
        """
        on_all_children('reset_frame', self)
