"""Lookup Module
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object
    """
    return list(dir(obj))
