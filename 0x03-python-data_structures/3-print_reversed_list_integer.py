#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list of integer values in reverse order

        Args:
        my_list: list of integers

        Returns:
        Does not return anything
    """
    size = len(my_list)
    if size > 0:
        for idx in range(0, size):
            print("{:d}".format(my_list[size-1-idx]))
