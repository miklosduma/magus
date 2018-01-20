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
    if value is None:
        return True

    elif value == '':
        return True

    else:
        return False


def validate_integer(n, min_val=0, max_val=99):
    """
    Validates an integer value. Not, all fields
    use string values, so n may be a string to begin with.

    The function will try to change n to an integer.
    """
    n = strip_if_string(n)

    if is_empty(n):
        raise FieldValidationError(EMPTY_FIELD)

    try:
        n = int(n)

        if not between_thresholds(n, min_val, max_val):
            raise FieldValidationError(NUMBER_LENGTH_ERROR.format(min_val,
                                                                  max_val))

        return n

    except ValueError as error:
        value = get_value_from_error(error.message)
        raise FieldValidationError(NOT_NUMBER.format(value))


def validate_string(s, min_length=3, max_length=12):
    """
    Validates a string. Checks whether it is
    an empty string or not.
    """
    s = strip_if_string(s)

    if is_empty(s):
        raise FieldValidationError(EMPTY_FIELD)

    length = len(s)

    if not between_thresholds(length, min_length, max_length):
        raise FieldValidationError(STRING_LENGTH_ERROR.format(min_length,
                                                              max_length))

    return s
