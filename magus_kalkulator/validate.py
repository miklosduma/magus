import re

EMPTY_FIELD = 'Tolts ki minden mezot!'
NOT_NUMBER = 'Nem szam: {}'
NEGATIVE_NUMBER = 'Adj meg pozitiv szamot e helyett: {}'

MATCH_SINGLE_QUOTES = r'\'[^\']+\''


def get_value_from_error(msg):
    """
    Uses regexp to retrieve the value
    from a ValueError exception.
    """
    return re.findall(MATCH_SINGLE_QUOTES, msg)[0]


def is_negative(number):
    """
    Returns True or False depending on whether
    the input number is smaller than zero.
    """
    return number < 0


def strip_if_string(value):
    try:
        return value.strip()
    except AttributeError as error:
        print(error)
        return value


def is_empty(value):
    value = strip_if_string(value)

    if value is None:
        return True

    elif value == '':
        return True

    else:
        return False


def validate_integer(n):
    if is_empty(n):
        return False, EMPTY_FIELD

    try:
        n = int(n)

        if is_negative(n):
            return False, NEGATIVE_NUMBER.format(n)
        return True, n

    except ValueError as error:
        value = get_value_from_error(error.message)
        return False, NOT_NUMBER.format(value)


def validate_string(s):
    if is_empty(s):
        return False, EMPTY_FIELD

    return True, s
