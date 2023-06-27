#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """My Safe Print List Function

    Args:
        my_list: list that can contain any type of data
        x: number of elements to print

    Returns:
        The returns a list of x elements
    """
    counter = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            counter += 1
        print("{}".format(""))
    except Exception:
        print("{}".format(""))
    return counter
