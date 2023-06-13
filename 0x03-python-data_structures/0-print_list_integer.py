#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print a list of integer values

        Args:
        my_list: list of integers

        Returns:
        Does not return anything
    """
    for element in (my_list):
        print("{:d}".format(element))
