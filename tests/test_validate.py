"""
Tests field validation for strings and integers.
"""

import pytest
from magus_kalkulator.validate import (validate_integer, validate_string,
                                       FieldValidationError)


TEST_DATA_VALIDATE_INT = [
    ('foo', {}, 'Nem szam: foo'),
    (-1, {}, 'Adj meg egy szamot 0 es 99 kozott!'),
    ('0', {'min_val': 1}, 'Adj meg egy szamot 1 es 99 kozott!'),
    ('1', {'min_val': 1}, 1),
    (' 11 ', {'min_val': 1}, 11),
    (99, {}, 99),
    (99, {'max_val': 30}, 'Adj meg egy szamot 0 es 30 kozott!')
]


@pytest.mark.parametrize('value,kwargs,expected',
                         TEST_DATA_VALIDATE_INT)
def test_validate_int(value, expected, kwargs):
    """
    Tests integer type field validation.
    """
    try:
        result = validate_integer(value, **kwargs)
        assert result == expected

    except FieldValidationError as error:
        assert error.message == expected


TEST_DATA_VALIDATE_STRING = [
    ('foo', {}, 'foo'),
    ('', {}, 'Tolts ki minden mezot!'),
    ('b', {'min_length': 1}, 'b'),
    ('  d  ', {'min_length': 1}, 'd'),
    ('ThisIsWayTooLongIThink', {}, ('Adj meg egy minimum 3 \nes '
                                    'maximum 12 karakter hosszu erteket!')),
    ('Haha', {'max_length': 4}, 'Haha')
]


@pytest.mark.parametrize('value,kwargs,expected',
                         TEST_DATA_VALIDATE_STRING)
def test_validate_str(value, expected, kwargs):
    """
    Tests string type field validation.
    """
    try:
        result = validate_string(value, **kwargs)
        assert result == expected

    except FieldValidationError as error:
        assert error.message == expected
