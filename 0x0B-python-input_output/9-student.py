#!/usr/bin/python3
"""Student Module
"""


class Student:
    """Class Student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize Method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert class to JSON string
        """
        return self.__dict__
