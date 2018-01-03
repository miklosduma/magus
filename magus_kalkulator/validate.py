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


def check_numbers(numbers):
    """
    Validates integer field values.
    Returns an error if the field value:
        - is not integer
        - is negative
    """
    for number in numbers:
        # Negative field value
        if is_negative(number):
            return False, NEGATIVE_NUMBER.format(number)

    return True, numbers


def validate_values(values, integers=None):
    """
    Validates the value of input fields.
    Specify the index of all integer fields in
    the integers key argument.
    """

    # Strip all values (at this stage they all must be strings)
    values = [x.strip() if isinstance(x, str) else x for x in values]

    # Find emtpy fields
    missing = [x for x in values if not x]

    if missing:
        return False, EMPTY_FIELD

    # If no integers are found, validation succeeds
    if not integers:
        return True, values

    # Find integer values and validate them
    try:
        values = [int(x) if values.index(x) in integers else x for x in values]

    except ValueError as error:
        value = get_value_from_error(error.message)
        return False, NOT_NUMBER.format(value)

    success, result = check_numbers(values)

    if success:
        return True, result

    # Return error message if validation fails
    return False, result