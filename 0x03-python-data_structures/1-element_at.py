#!/usr/bin/python3
def element_at(my_list, idx):
    """Gets an element at given index of a list

        Args:
        my_list: list of integers
        idx: index of element

        Returns:
        Returns None if idx is greater than size of list or negative
        else returns the value of the list at given index
    """
    if idx < 0 or idx >= len(my_list):
        return "None"
    else:
        return my_list[idx]
