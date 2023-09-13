#!/usr/bin/python3
"""Read File Module
"""


def read_file(filename=""):
    """Read file and print to stdout

        Arg:
            filename: name of file
    """
    with open(filename, 'r', encoding='utf-8') as file_reader:
        print(file_reader.read())
