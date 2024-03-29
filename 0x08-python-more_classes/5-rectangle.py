#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle class
    """
    def __init__(self, width=0, height=0):
        """Initializing Method

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
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Get the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __print__(self):
        """Return a square object"""
        stringbuilder = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                stringbuilder += "#"
            stringbuilder += "\n"
        return stringbuilder[0:-1]

    def __str__(self):
        """Return a square object"""
        stringbuilder = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                stringbuilder += "#"
            stringbuilder += "\n"
        return stringbuilder[0:-1]

    def __repr__(self):
        """Returns a string representation of the Rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        del self
