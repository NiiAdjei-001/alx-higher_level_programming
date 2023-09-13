#!/usr/bin/python3
"""Read File Module
"""


def read_file(filename=""):
    """Read File and print to stdout
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file_reader:
            print(file_reader.read())
    except Exception:
        pass
