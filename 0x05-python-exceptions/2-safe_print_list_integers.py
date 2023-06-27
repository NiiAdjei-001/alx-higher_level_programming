#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """My Safe Print List Integer Function

    Args:
        my_list: list that can contain any type of data
        x: number of elements to print

    Returns:
        The returns a list of x elements
    """
    counter = 0
    try:
        for ite in range(x):
            if type(my_list[ite]) == int:
                print("{:d}".format(my_list[ite]), end="")
                counter += 1
        print("{}".format(""))
    except Exception:
        print("{}".format(""))
    return counter
