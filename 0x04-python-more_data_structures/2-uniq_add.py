#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list

        Args:
        my_list: list of integers

        Returns:
        Returns the sum of unique integers
    """
    my_set = set(my_list)
    my_sum = 0
    for element in my_set:
        my_sum += element
    return my_sum
