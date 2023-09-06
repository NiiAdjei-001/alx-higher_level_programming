#!/usr/bin/python3
"""Say my name Module
"""


def say_my_name(first_name, last_name=""):
    """Say my name function

    Args
        first_name: first name string
        last_name: last name string

    Return:
        returns full name
    """
    if not (type(first_name) == str):
        raise TypeError("first_name must be a string")
    if not (type(last_name) == str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
