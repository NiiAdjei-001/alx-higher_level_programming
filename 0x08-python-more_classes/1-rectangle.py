#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """Initilizing Method
        """
        if not (type(width) is int or type(height) is int):
            raise TypeError
        if width < 0 or height < 0:
            raise ValueError
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if width is not int:
            raise TypeError
        if width < 0:
            raise ValueError
        self.__width = value
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if height is not int:
            raise TypeError
        if height < 0:
            raise ValueError
        self.__height = value
