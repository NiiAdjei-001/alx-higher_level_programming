#!/usr/bin/python3
"""Append Write To File Module
"""


def append_write(filename="", text=""):
    """Appends a text to a file
    """
    with open(filename, 'a+', encoding='utf-8') as file_appender:
        return file_appender.write(text)
