#!/usr/bin/python3
"""Inherits from
"""


def inherits_from(obj, a_class):
    """ inherits_from: checks if an object is a direct or
        indirect subclass of a specified class

        Args:
            obj: object to run check on
            a_class: class value to check against

        Return:
            True - if class of obj is a subclass of a_class
            False - otherwise
    """
    if issubclass(obj.__class__, a_class) and obj.__class__ != a_class:
        return True
    return False
