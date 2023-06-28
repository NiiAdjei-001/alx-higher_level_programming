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
        try:
            self.__size = size
            if type(self.__size) != int:
                raise TypeError
            if self.__size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
