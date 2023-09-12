#!/usr/bin/python3
"""Is Same Class Module"""


def is_same_class(obj, a_class):
    """is_same_class method
        Arg:
            obj: instantiated object
            a_class: class object
        Returns True if obj matches class specified by a_class else False
    """
    if obj.__class__ == a_class:
        return True
    return False
