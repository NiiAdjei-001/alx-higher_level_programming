#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """Initilizing Method

            Args
                width: rectangle width
                height: rectangle height
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Gets width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle h x w
        """
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle 2 x (h + w)
        """
        return 2 * ( self.__height + self.__width)
