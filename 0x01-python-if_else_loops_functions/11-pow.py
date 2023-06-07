#!/usr/bin/python3
def pow(a, b):
    res = 1
    for i in range(0, abs(b)):
        if b > 0:
            res *= a
        elif b == 0:
            pass
        else:
            res *= 1/a
    return res
