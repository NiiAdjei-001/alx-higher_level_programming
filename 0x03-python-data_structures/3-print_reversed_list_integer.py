#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list of integer values in reverse order

        Args:
        my_list: list of integers

        Returns:
        Does not return anything
    """
    for idx in range(0, len(my_list)):
        print("{:d}".format(my_list[-1-idx]))
