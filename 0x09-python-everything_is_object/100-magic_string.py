#!/usr/bin/python3
ls=[]
def magic_string():
    ls.append('BestSchool') if len(ls) == 0 else ls.append(', BestSchool')
    return ''.join(ls)
