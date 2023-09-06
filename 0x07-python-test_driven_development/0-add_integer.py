#!/usr/bin/python3
"""Add Integer Module
"""


def add_integer(a, b=98):
    """Adds two integers

        Args
            a: first integer
            b: second integer

            Return:
                returns the sum of the two integers
    """
    if not (type(a) == int or type(a) == float):
        raise TypeError("a must be an integer")
    if not (type(b) == int or type(b) == float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
