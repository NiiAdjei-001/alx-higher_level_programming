#!/usr/bin/python3
"""Base Model Module
"""
import json
import csv


class Base:
    """Bass Class
    """
    __nb_object = 0
    """Number of object instances"""

    def __init__(self, id=None):
        """Init Method

            Arg:
                id: (optional) id for object instance
        """
        if (id is None):
            type(self).__nb_object += 1
            self.id = self.__nb_object
        else:
            # type(self).__nb_object += 1
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of objects into a list of serialized objects"""
        if (list_dictionaries is None):
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """converts a json string into a json object"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a class from """
        dummy: cls = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of serialized objects into a json file"""
        filename = "{}.json".format(cls.__name__)
        json_list_objs = []
        for item in list_objs:
            json_list_objs.append(item.to_dictionary())
        with open(filename, 'w') as file_writer:
            return file_writer.write(Base.to_json_string(json_list_objs))

    @classmethod
    def load_from_file(cls):
        """Loads a list of deserialized objects from a json file"""
        filename = "{}.json".format(cls.__name__)
        json_list_objs = []
        with open(filename, 'r') as file_reader:
            json_string = file_reader.read()
            json_list_dict = Base.from_json_string(json_string)
            for item in json_list_dict:
                json_list_objs.append(cls.create(**item))
        return json_list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves a list of serialized objects into a csv file"""
        filename = "{}.csv".format(cls.__name__)
        pass

    @classmethod
    def load_from_file_csv(cls, list_objs):
        """Loads a list of deserialized objects from a csv file"""
        filename = "{}.csv".format(cls.__name__)
        pass
