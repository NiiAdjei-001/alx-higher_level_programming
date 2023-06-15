#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key value pair from a dictionary

        Args:
        a_dictionary: A dictionary
        key: key

        Returns:
        returns a dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
