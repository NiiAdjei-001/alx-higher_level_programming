#!/usr/bin/python3
"""Magic String Function Module"""


ls = []


def magic_string():
    """Magic String Function"""
    ls.append('BestSchool') if len(ls) == 0 else ls.append(', BestSchool')
    return ''.join(ls)
