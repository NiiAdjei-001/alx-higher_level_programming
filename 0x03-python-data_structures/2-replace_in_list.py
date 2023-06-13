#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element in a particular index of a list

        Args:
        my_list: list of integers
        idx: index of element
        element: new element to replace existing index value

        Returns:
        Returns unaugmented list if idx is negative
        or greater than list size
        else returns augmented list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
