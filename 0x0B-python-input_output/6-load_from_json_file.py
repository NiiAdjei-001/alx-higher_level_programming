#!/usr/bin/python3
"""Create object from JSON file
"""


import json


def load_from_json_file(filename):
    """Load Object from JSON file
    """
    with open(filename, 'r') as file_reader:
        json_string = file_reader.read()
        json_object = json.loads(json_string)
        return json_object
