#!/usr/bin/python3
def magic_string(ls=[]):
    ls.append('BestSchool') if len(ls) == 0 else ls.append(', BestSchool')
    return ''.join(ls)
