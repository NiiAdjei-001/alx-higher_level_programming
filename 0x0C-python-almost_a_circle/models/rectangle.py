#!/usr/bin/python3
"""Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        if not (type(width) is int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not (type(height) is int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not(type(x) is int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not(type(y) is int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not (type(value) is int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not (type(value) is int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set width"""
        if not(type(value) is int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get height"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set height"""
        if not (type(value) is int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Gets the area if the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle image"""
        row = ''
        for xpos in range(self.__x):  # emulate display position at x
            row += ' '
        for w in range(self.__width):  # emulate display of width
            row += '#'
        for ypos in range(self.__y):  # emulate display position at y
            print()
        for h in range(self.__height):  # emulate display of height
            print(row)

    def __str__(self):
        """To string method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Update with *args => (id, width, height, x, y)"""
        if (args and args is not None):
            if (args.__len__() > 0):
                self.id = args[0]
            if (args.__len__() > 1):
                self.width = args[1]
            if (args.__len__() > 2):
                self.height = args[2]
            if (args.__len__() > 3):
                self.x = args[3]
            if (args.__len__() > 4):
                self.y = args[4]
        else:
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            if 'width' in kwargs.keys():
                self.width = kwargs['width']
            if 'height' in kwargs.keys():
                self.height = kwargs['height']
            if 'x' in kwargs.keys():
                self.x = kwargs['x']
            if 'y' in kwargs.keys():
                self.y = kwargs['y']

    def to_dictionary(self):
        """return a dictionary object of class instance"""
        dictionary = dict(
            id=self.id,
            width=self.width,
            height=self.height,
            x=self.x,
            y=self.y
        )
        return dictionary
