"""
Main module for individual character class and characters master class.
"""

from __future__ import print_function


class Karakter:
    """
    Class for adding individual characters.
    """
    def __init__(self, name, max_ep, sfe, max_fp=None):
        """
        Initialising new character.
            - name:
                The name of the new character
                It will also be used as the index
                of the character
            - ep:
                The maximum EP of the character. At startup
                also used to set akt_ep
            - sfe:
                The SFE of the character. Will be a map later on
            - fp:
                The maximum FP of the character. At startup also used
                to set akt_fp. Undeads and similar have no FP
        """
        self.name = name
        self.max_ep = max_ep
        self.akt_ep = max_ep
        self.max_fp = max_fp
        self.akt_fp = max_fp
        self.sfe = sfe


class Karakterek:
    """
    Class for storing and maintaining existing characters.
    """
    def __init__(self):
        """
        Initialise dictionary that holds character objects.
        """
        self.karakterek = {}

    def add_karakter(self, name, max_ep, sfe, max_fp=None):
        """
        Adds a new character to the characters map.
        The param 'name' is also used as the key of the new
        record.

        Names therefore must be unique across characters.
        """
        # Check whether name already exists. If yes, do not overwrite.
        if any(existing_name == name for
               existing_name in self.get_all_karakters()):
            return False, 'Karakter mar letezik!'

        # Create new character and add to characters map using name as key
        self.karakter = Karakter(name, max_ep, sfe, max_fp)
        self.karakterek[self.karakter.name] = self.karakter
        return True, 'Karakter hozzaadva!'

    def get_karakter(self, name):
        """
        Retrieves a character object from
        the characters map based on its name.
        """
        try:
            return self.karakterek[name]
        except KeyError:
            return 'Nincs ilyen karakter!'

    def delete_karakter(self, name):
        """
        Deletes a character from the characters map
        based on its name.
        """
        del self.karakterek[name]

    def get_all_karakters(self):
        """
        Returns the name of all characters kept
        in memory.
        """
        return self.karakterek.keys()
