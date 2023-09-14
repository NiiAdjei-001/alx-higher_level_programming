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

    def to_json(self, attrs=None):
        """Convert class to JSON string
        """
        if attrs is None:
            return self.__dict__
        json_string = dict(self.__dict__)
        for key in attrs:
            if key in json_string.keys():
                del json_string[key]
        # print("python obj: " + str(self.__dict__))
        # print("json_obj: " + str(json_string))
        return json_string

    def reload_from_json(self, json):
        for key, value in json.items():
            # print("key: {} value: {}".format(key, value))
            setattr(self, key, value)
