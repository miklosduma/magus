from magus_kalkulator.karakterek import Karakter, Karakterek


def test_new_karakter_no_fp():
    """
    Tests creation of new character.
    """
    foo = Karakter('Foo', 13, 3)
    assert foo.name == 'Foo'
    assert foo.max_ep == 13
    assert foo.akt_ep == 13
    assert foo.sfe == 3
    assert not foo.akt_fp
    assert not foo.max_fp


def test_new_karakter_fp():
    """
    Tests creation of new character.
    """
    bar = Karakter('Bar', 15, 0, fp=33)
    assert bar.name == 'Bar'
    assert bar.max_ep == 15
    assert bar.akt_ep == 15
    assert bar.sfe == 0
    assert bar.akt_fp == 33
    assert bar.max_fp == 33


def test_karakterek():
    """
    Tests addition/deletion of characters
    to characters object.
    """
    karakterek = Karakterek()
    assert not karakterek.karakterek

    karakterek.add_karakter('Sam', 14, 5)
    sam = karakterek.get_karakter('Sam')
    assert sam.name == 'Sam'
    assert sam.max_ep == 14
    assert sam.sfe == 5

    # Character cannot be accidentally overwritten by
    # being added a second time
    karakterek.add_karakter('Sam', 15, 7)
    sam = karakterek.get_karakter('Sam')
    assert sam.name == 'Sam'
    assert sam.max_ep == 14
    assert sam.sfe == 5

    # Add second character with fp
    karakterek.add_karakter('Esme', 13, 0, fp=44)
    esme = karakterek.get_karakter('Esme')
    assert esme.name == 'Esme'
    assert esme.akt_fp == 44
    assert esme.max_fp == 44

    # Check if all names are added successfully
    karakter_nevek = karakterek.get_all_karakters()
    assert all(name in karakter_nevek for name in ['Esme', 'Sam'])

    karakterek.delete_karakter('Sam')
    sam = karakterek.get_karakter('Sam')
    karakterek.delete_karakter('Esme')
    karakter_nevek = karakterek.get_all_karakters()
    assert not all(name in karakter_nevek for name in ['Esme', 'Sam'])
    assert sam == 'Nincs ilyen karakter!'



