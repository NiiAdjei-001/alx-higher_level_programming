#!/usr/bin/python3
"""This module defines a square class
"""


class Square:
    """Square class
        Used to create a square object
    """
    def __init__(self, size):
        """__init__ method
            Initializes the square object

            Args:
                size: length of the square
        """
        self.__size = size
