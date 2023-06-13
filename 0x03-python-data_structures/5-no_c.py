#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string

        Args:
        my_string: string value

        Returns:
        Returns new string without c or C character
    """
    new_string = ""
    for element in my_string:
        if element == 'c' or element == 'C':
            pass
        else:
            new_string += element
    return new_string
