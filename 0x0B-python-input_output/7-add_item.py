#!/usr/bin/python3
"""Adds Python Arguments to a list and then saves them to a file Module
"""


import json
import sys
from os.path import isfile


filename = "add_item.json"
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def run():
    """ run script
    """
    if not isfile(filename):
        with open(filename, 'w') as fw:
            fw.write("[]")
    file_content = load_from_json_file(filename)
    file_content.extend(sys.argv[1:])
    save_to_json_file(file_content, filename)


run()
