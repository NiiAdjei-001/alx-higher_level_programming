#!/usr/bin/python3
"""JSON String to JSON Object Converter Module"""


import json


def from_json_string(my_str):
    """Converts a json string into JSON object

        Args:
            my_str: json string

        Returns: Python Object from json string
    """
    json_object = json.loads(my_str)
    return json_object
