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
        self.__size = size

    def area(self):
        """Returns the area of the square

            Returns:
                size * size
        """
        return self.__size * self.__size
    
    @property
    def size(self):
        """Returns the size of the square

            Returns:
                size
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """Sets the size of the square
            
            Args:
                value: new value of size
        """
        if not (type(value) == int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
