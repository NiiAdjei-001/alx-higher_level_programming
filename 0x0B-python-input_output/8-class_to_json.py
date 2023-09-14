#!/usr/bin/python3
"""Class to JSON Module
"""


def class_to_json(obj):
    """Converts an instance of a class into JSON object
    """
    return obj.__dict__
