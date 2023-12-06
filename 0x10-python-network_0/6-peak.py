#!/usr/bin/python3
"""Find the peak module"""


def find_peak(list_of_integers):
    """Finds the peak value of a list of integers`"""
    peak = -9223372036854775807
    if list_of_integers is None:
        return None
    for val in set(list_of_integers):
        if val > peak:
            peak = val
    return peak
