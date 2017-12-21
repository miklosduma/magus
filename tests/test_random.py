import pytest

from magus_kalkulator.random_body import (add_n_times_to_list, build_main_table,
                               get_sub_parts, pick_sub_parts)


def test_add_n_times_to_list_no_list():
    """
    Tests addition of a value to a list one or more times.
    No starting list is specified.
    """
    result = add_n_times_to_list('foo', 3)
    assert result == ['foo', 'foo', 'foo']


def test_add_n_times_to_list():
    """
    Tests addition of a value to a list one or more times.
    A starting list is specified.
    """
    result = add_n_times_to_list('bar', 2,candidates=['foo', 'foo'])
    assert result.count('foo') == 2
    assert result.count('bar') == 2


def test_build_main():
    """
    Test if build main table function
    returns a list containing the right
    number of fej(1), torzs(4) and vegtag(5).
    """
    result = build_main_table()
    assert result.count('Fej') == 1
    assert result.count('Torzs') == 4
    assert result.count('Jkez') == 2
    assert result.count('Bkez') == 1
    assert result.count('Jlab') == 1
    assert result.count('Blab') == 1


def test_get_sub_parts():
    """
    Tests if all correct sub parts are returned.
    """
    result = get_sub_parts('Fej')
    assert result.count(('Koponya', 'Koponya')) == 3
    assert result.count(('Koponya', 'Homlok')) == 2
    assert result.count(('Koponya', 'Halantek')) == 1
    assert result.count(('Arc', 'Arc')) == 2
    assert result.count(('Nyak', 'Nyak')) == 2

def test_pick_sub_parts():
    """
    Tests sub part selection.
    Expects a tuple.
    """
    pen_part, sfe_part = pick_sub_parts()
    assert all(isinstance(x, str) for x in (pen_part, sfe_part))

def test_pick_sub_parts_specific():
    """
    Tests sub part selection.
    Expects a tuple.
    """
    pen_part, sfe_part = pick_sub_parts(main_part='Jkez')
    assert all(isinstance(x, str) for x in (pen_part, sfe_part))
    assert pen_part == 'Jkez'
    assert  sfe_part in ['Jfelkar', 'Jkonyok', 'Jalkar', 'Jcsuklo', 'Jkezfej',
                         'Jvall']