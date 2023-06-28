#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """My List division function. divides content of my_list_1 by my_list_2

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: length of list to access.

    Returns:
        The returns list with divided results
    """
    pos = 0
    val = 0
    result = []
    errorChecks = [ZeroDivisionError, TypeError, IndexError]
    for pos in range(list_length):
        try:
            val = my_list_1[pos] / my_list_2[pos]
        except ZeroDivisionError as err:
            result.append(0)
            print("division by 0")
        except TypeError as err:
            result.append(0)
            print("wrong type")
        except IndexError as err:
            result.append(0)
            print("out of range")
        else:
            result.append(val)
        finally:
            pass
    return result
