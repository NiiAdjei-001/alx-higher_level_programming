#!/usr/bin/python3
"""This module defines a square class
"""


class Square:
    """Square class
        Used to create a square object
    """
    def __init__(self, size=0):
        """__init__ method
            Initializes the square object

            Args:
                size: length of the square
        """
        if not (type(size) == int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
