#!/usr/bin/python3
l = []
def magic_string():
    l.append('BestSchool') if len(l) == 0 else l.append(', BestSchool')
    return ''.join(l)
