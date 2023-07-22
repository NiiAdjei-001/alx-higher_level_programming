#!/usr/bin/python3
""" Print square module
"""


def print_square(size):
    """Print square function

        Args:
        size: length of the square
    """
    if not type(size) in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for r in range(size):
        for c in range(size):
            print("#", end="")
        print("")
