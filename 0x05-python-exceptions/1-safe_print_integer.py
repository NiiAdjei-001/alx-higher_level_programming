#!/usr/bin/python3
def safe_print_integer(value):
    """My Safe Print Integer List

    Args:
        value: value to be printed

    Returns:
        The returns True if element is an Integer else False
    """
    state = False
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
