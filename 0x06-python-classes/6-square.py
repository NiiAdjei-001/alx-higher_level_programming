#!/usr/bin/python3
"""This module defines a square class
"""
type_err_mes_size = "size must be an integer"
value_err_mes_size = "size must be >= 0"
type_err_mes_position = "position must be a tuple of 2 positive integers"


class Square:
    """Square class
        Used to create a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method
            Initializes the square object

            Args:
                size: length of the square
        """
        if not (type(size) == int):
            raise TypeError(__type_err_mes_size)
        if size < 0:
            raise ValueError(__value_err_mes_size)
        if not (type(position) == tuple):
            raise TypeError(type_err_mes_position)
        if len(position) != 2:
            raise TypeError(type_err_mes_position)
        if not ((type(position[0]) == int) and (type(position[1]) == int)):
            raise TypeError(type_err_mes_position)
        if ((position[0] < 0) or (position[1] < 0)):
            raise TypeError(type_err_mes_position)
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the area of the square

            Returns:
                size * size
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the square

            Returns:
               size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Sets the size of the square

            Args:
                size: x unit
        """
        if not (type(size) == int):
            raise TypeError(__type_err_mes_size)
        if size < 0:
            raise ValueError(__value_err_mes_size)
        self.__size = size

    @property
    def position(self):
        """Gets the position coordinates of the square

            Returns:
                position
        """
        return self.__position

    @position.setter
    def position(self, position):
        """Sets the position coordinates of the square

            Args:
                position: position coordinates (x, y)
        """
        if not ((type(position[0]) == int) and (type(position[1]) == int)):
            raise TypeError(__type_err_mes_position)
        if ((position[0] <= 0) or (postion[1] < 0)):
            raise TypeError(__type_err_mes_position)
        self.__position = position

    def area(self):
        """Returns the area of the square

        Returns:
            size * size
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints a square
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for row in range(0, self.__size):
                for col in range(0, self.__size + self.__position[0]):
                    if col < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
