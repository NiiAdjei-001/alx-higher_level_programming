#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary in ordered keys

        Args:
        a_dictionary: A dictionary

        Returns:
        Nothing
    """
    s_keys = sorted(list(a_dictionary))
    for element in s_keys:
        print("{}: {}".format(element, a_dictionary[element]))
