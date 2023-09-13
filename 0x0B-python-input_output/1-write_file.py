#!/usr/bin/python3
"""Write To  File Module
"""


def write_file(filename="", text=""):
    """Write a text to a file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file_writer:
            return file_writer.write(text)
    except Exception as error:
        print(error)
