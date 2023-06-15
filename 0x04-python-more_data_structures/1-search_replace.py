#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces every occurance of an element with another in a list

        Args:
        my_list: list of integers
        search: element to be replaced
        replace: element to replace

        Returns:
        Returns a new list of replaced values
    """
    new_list = []
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
    return new_list
