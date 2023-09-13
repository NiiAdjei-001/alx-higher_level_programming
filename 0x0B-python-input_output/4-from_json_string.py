#!/usr/bin/python3
"""JSON String to Object Module
"""


import json


def from_json_string(my_str):
    return json.loads(my_str)
