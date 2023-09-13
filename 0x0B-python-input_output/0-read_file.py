#!/usr/bin/python3
"""Read File Module
"""


def read_file(filename=""):
    """Read File and print to stdout
    """
    with open(filename, 'r', encoding='utf-8') as _file:
        print(_file.read())
