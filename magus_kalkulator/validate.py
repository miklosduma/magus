"""
Functions to validate string or integer values.
"""

import re

EMPTY_FIELD = 'Tolts ki minden mezot!'
NOT_NUMBER = 'Nem szam: {}'
NEGATIVE_NUMBER = 'Adj meg pozitiv szamot e helyett: {}'

NUMBER_LENGTH_ERROR = 'Adj meg egy szamot {} es {} kozott!'
STRING_LENGTH_ERROR = ('Adj meg egy minimum {} \nes maximum {}'
                       ' karakter hosszu erteket!')

MATCH_SINGLE_QUOTES = r'\'[^\']+\''


class FieldValidationError(Exception):
    """
    Exception raised on validation failures.
    """

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


def get_value_from_error(msg):
    """
    Uses regexp to retrieve the value
    from a ValueError exception.
    """
    return re.findall(MATCH_SINGLE_QUOTES, msg)[0]


def between_thresholds(value, min_val, max_val):
    """
    Checks whether value falls between min_val and
    max_val.
    """
    return min_val <= value <= max_val


def strip_if_string(value):
    """
    Removes leading and trailing spaces
    from a string.

    If value is not a string, returns it
    as it is.
    """
    try:
        return value.strip()

    except AttributeError as error:
        print(error)
        return value


def is_empty(value):
    """
    Checks if a value is an empty string or None.
    """
    if value is None or value == '':
        return True

    return False


def validate_integer(number, min_val=0, max_val=99):
    """
    Validates an integer value. Not, all fields
    use string values, so n may be a string to begin with.

    The function will try to change n to an integer.
    """
    number = strip_if_string(number)

    if is_empty(number):
        raise FieldValidationError(EMPTY_FIELD)

    try:
        number = int(number)

        if not between_thresholds(number, min_val, max_val):
            error_msg = NUMBER_LENGTH_ERROR.format(min_val, max_val)
            raise FieldValidationError(error_msg)

        return number

    except ValueError:
        raise FieldValidationError(NOT_NUMBER.format(number))


def validate_string(string, min_length=3, max_length=12):
    """
    Validates a string. Checks whether it is
    an empty string or not.
    """
    string = strip_if_string(string)

    if is_empty(string):
        raise FieldValidationError(EMPTY_FIELD)

    length = len(string)

    if not between_thresholds(length, min_length, max_length):
        error_msg = STRING_LENGTH_ERROR.format(min_length, max_length)
        raise FieldValidationError(error_msg)

    return string
