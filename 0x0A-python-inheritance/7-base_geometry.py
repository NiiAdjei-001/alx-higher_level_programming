#!/usr/bin/python3
"""BaseGeometry Module
"""


class BaseGeometry:
    """Base Geometry Class
    """
    def __init__(self):
        """Initialize Object
        """
        pass

    def area(self):
        """Compute Object Area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
