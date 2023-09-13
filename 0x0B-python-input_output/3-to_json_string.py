#!/usr/bin/python3
"""To JSON string Module
"""


import json


def to_json_string(my_obj):
    """Converts an object to a JSON string
    """
    return json.dumps(my_obj)
