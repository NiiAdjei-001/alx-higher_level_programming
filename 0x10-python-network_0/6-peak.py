#!/usr/bin/python3
"""Find the peak module"""
import sys


def find_peak(list_of_integers):
    peak = -1 * sys.maxsize
    if list_of_integers is None:
        return None
    for val in list_of_integers:
        if val > peak:
            peak = val
    return peak
