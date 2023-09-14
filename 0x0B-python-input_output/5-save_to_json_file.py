#!/usr/bin/python3
"""Save JSON objec to file Module
"""


import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a JSON file

        Args:
            my_obj: object
            filename: file name
    """
    with open(filename, 'w') as file_writer:
        serialized_object = json.dumps(my_obj)
        return file_writer.write(serialized_object)
