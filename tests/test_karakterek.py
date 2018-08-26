"""
Tests creation and modification of characters.
"""
import magus_kalkulator.magus_constants as mgc
from magus_kalkulator.karakterek import Characters


def test_karakterek():
    """
    Tests addition/deletion of characters
    to characters object.
    """
    karakterek = Characters()
    assert not karakterek.character_maps

    karakterek.add_character('Sam', {mgc.MAX_EP: 14, mgc.NAME: 'Sam'})
    sam = karakterek.get_character('Sam')
    assert sam[mgc.NAME] == 'Sam'
    assert sam[mgc.MAX_EP] == 14

    # Character cannot be accidentally overwritten by
    # being added a second time
    karakterek.add_character('Sam', {mgc.MAX_EP: 15, mgc.NAME: 'Sam'})
    sam = karakterek.get_character('Sam')
    assert sam[mgc.NAME] == 'Sam'
    assert sam[mgc.MAX_EP] == 14

    # Add second character with fp
    karakterek.add_character('Esme', {mgc.MAX_FP: 44, mgc.NAME: 'Esme'})
    esme = karakterek.get_character('Esme')
    assert esme[mgc.NAME] == 'Esme'
    assert esme[mgc.MAX_FP] == 44

    # Check if all names are added successfully
    karakter_nevek = karakterek.get_character_names()
    assert all(name in karakter_nevek for name in ['Esme', 'Sam'])

    karakterek.delete_character('Sam')
    sam = karakterek.get_character('Sam')
    karakterek.delete_character('Esme')
    karakter_nevek = karakterek.get_character_names()
    assert not all(name in karakter_nevek for name in ['Esme', 'Sam'])
    assert sam == 'Nincs ilyen karakter!'
