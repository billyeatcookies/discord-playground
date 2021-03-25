import re


def alphanumeric(string):
    """
    Validate if a user input string is alphanumeric.
    """
    return bool(re.match(r'^[A-Za-z0-9]+$', string))
