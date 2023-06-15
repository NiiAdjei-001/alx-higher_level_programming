#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Finds elements that are present in only one set

        Args:
        set_1: set 1
        set_2: set 2

        Returns:
        Returns a list of none common elements
    """
    return set_1 ^ set_2
