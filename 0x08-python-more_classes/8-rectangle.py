#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Rectangle class
    """

    number_of_instances = 0
    """Count of number of instances of Rectangle object"""

    print_symbol = "#"
    """Symbol to use to print Rectangle object"""

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
        type(self).number_of_instances += 1

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
                stringbuilder += str(self.print_symbol)
            stringbuilder += "\n"
        return stringbuilder[0:-1]

    def __str__(self):
        """Return a square object"""
        stringbuilder = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                stringbuilder += str(self.print_symbol)
            stringbuilder += "\n"
        return stringbuilder[0:-1]

    def __repr__(self):
        """Returns a string representation of the Rectangle object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
        del self

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
