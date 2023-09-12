#!/usr/bin/python3
"""Is Kind Of Class
"""


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class: checks if an object is a specified class
        or subclass of a specified class

        Args:
            obj: object to run check on
            a_class: class value to check against

        Return:
            True - if class of obj is a_class or if class of obj
            is a subclass of a_class
            False - otherwise
    """
    if obj.__class__ is a_class:
        return True
    if issubclass(obj.__class__, a_class):
        return True
    return False
