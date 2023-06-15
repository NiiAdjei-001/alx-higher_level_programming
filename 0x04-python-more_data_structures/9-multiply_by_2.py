#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Creates a new dictionary with all values multiplied by 2

        Args:
        a_dictionary: A dictionary

        Returns:
        returns a new dictionary
    """
    new_dictionary = a_dictionary.copy()
    keys = set(list(new_dictionary))
    for key in keys:
        new_dictionary[key] = 2 * new_dictionary[key]
    return new_dictionary
