#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print s a list of integer values

        Args:
        my_list: list of integers

        Returns:
        Does not return anything
    """
    for i in range(0, len(my_list)):
        print("{}".format(my_list[i]))
