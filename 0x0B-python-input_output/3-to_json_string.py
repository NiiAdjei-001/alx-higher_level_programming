#!/usr/bin/python3
"""Python object convert to JSON string Module
"""


import json


def to_json_string(my_obj):
    """Converts an object to a JSON string

        Args:
            my_obj: any python object

        Returns: json string of my_obj
    """
    json_string = json.dumps(my_obj)
    return json_string
