#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in index of a new copy of list

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
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
