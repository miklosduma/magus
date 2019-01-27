"""
Character management. E.g deleting characters or saving/loading.
"""
from __future__ import print_function

import os
from tkinter import ttk, VERTICAL, filedialog, messagebox, E, W

import webbrowser

from magus_kalkulator.interface_elements import organize_rows_to_left, \
    ChooseCharacterFrame, on_all_children, save_characters, load_characters, \
    CharacterValueField

from magus_kalkulator.validate import validate_string, FieldValidationError

from magus_kalkulator.table_to_html import target_dicts_to_html


def show_tables(*_args):
    """
    Generates an HTML output from the penalty
    tables and open the HTML file in the browser.
    """
    path = target_dicts_to_html()
    webbrowser.open(path)


class ManagementPage(ttk.Frame):
    """
    Adding characters main page.
    """
    def __init__(self, master, characters, messages):
        """
        Initialise management page.
        """
        ttk.Frame.__init__(self, master)
        self.main_panel = CharacterPanel(self, characters, messages)
        self.main_panel.grid()

    def reset_page(self):
        """
        Resets all child widgets of the frame.
        """
        on_all_children('reset_panel', self)


class CharacterPanel(ttk.PanedWindow):
    """
    Main panel of damage page.
    """
    def __init__(self, manage_page, characters, messages, orient=VERTICAL):
        """
        Initialise main panel.
        """
        ttk.PanedWindow.__init__(self, manage_page, orient=orient)
        self.characters = characters
        self.messages = messages
        self.choose_frame = ChooseCharacterFrame(self, self.characters)

        del_button = ttk.Button(self, text='Torles')
        del_button.bind('<Button-1>', self.del_character)

        save_load_frame = SaveLoadFrame(self, characters, messages)
        tables_frame = TablesFrame(self)
        # Place elements on grid
        final_row = organize_rows_to_left([save_load_frame,
                                           tables_frame,
                                           self.choose_frame], 0)
        del_button.grid(row=final_row, column=0, padx=2, pady=2, sticky=W)

    def reset_panel(self):
        """
        Resets all child widgets of this panel.
        """
        on_all_children('reset_frame', self)

    def del_character(self, *_args):
        """
        Deletes the selected character.
        """
        success, selected = self.choose_frame.get_selected()

        if success:
            self.characters.delete_character(selected)
            self.choose_frame.reset_frame()

            # Update characters kept in memory
            save_characters(self.characters.character_maps)

        else:
            self.messages.write_message(selected)


class SaveLoadFrame(ttk.LabelFrame):
    def __init__(self, panel, characters, messages):
        self.messages = messages
        self.characters = characters
        ttk.LabelFrame.__init__(self, panel, text='Save/Load')
        load_button = ttk.Button(self, text='Load')
        load_button.bind('<Button-1>', self.load_char)

        self.save_text = CharacterValueField(self, validate_string)
        save_button = ttk.Button(self, text='Save')
        save_button.bind('<Button-1>', self.save_char)
        self.save_text.grid(row=0)
        save_button.grid(row=1, sticky=W, pady=6)
        load_button.grid(row=1, sticky=E, pady=6)

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


class TablesFrame(ttk.LabelFrame):
    def __init__(self, panel):
        ttk.LabelFrame.__init__(self, panel, text='Sebzes tablazat')
        table_button = ttk.Button(self, text='Megnezem')
        table_button.bind('<Button-1>', show_tables)
        table_button.grid()
