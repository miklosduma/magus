"""
Main module for individual character class and characters master class.
"""

from __future__ import print_function


class Character:
    """
    Class for adding individual characters.
    """
    def __init__(self, name, values):
        """
        Initialising new character.
            - name:
                The name of the new character
                It will also be used as the index
                of the character
            - values:
                A map containing all information about the
                character, such as his/her EP/FP and SFE (another map)
        """
        self.name = name
        self.values = values


class Characters:
    """
    Class for storing and maintaining existing characters.
    """
    def __init__(self):
        """
        Initialise dictionary that holds character objects.
        """
        self.character_maps = {}

    def add_character(self, name, values):
        """
        Adds a new character to the characters map.
        The param 'name' is also used as the key of the new
        record.

        Names therefore must be unique across characters.
        """
        # Check whether name already exists. If yes, do not overwrite.
        if any(existing_name == name for
               existing_name in self.get_character_names()):
            return False, 'Karakter mar letezik!'

        # Create new character and add to characters map using name as key
        character = Character(name, values)
        self.character_maps[character.name] = character
        return True, 'Karakter hozzaadva!'

    def get_character(self, name):
        """
        Retrieves a character object from
        the characters map based on its name.
        """
        try:
            return self.character_maps[name]
        except KeyError:
            return 'Nincs ilyen karakter!'

    def delete_character(self, name):
        """
        Deletes a character from the characters map
        based on its name.
        """
        del self.character_maps[name]

    def get_character_names(self):
        """
        Returns the name of all characters kept
        in memory.
        """
        return self.character_maps.keys()

    def delete_all_characters(self):
        self.character_maps = {}
