#!/usr/bin/python3
def uppercase(str):
    l = len(str)
    for i in range(0, l):
        ci = ord(str[i]) # character's ascii number
        c = chr(ci - 32) # character offset by -32
        if ci >= 97 and ci <= 122:
            print("{}".format( (c + "\n") if (i == (l - 1)) else c), end="")
        else:
            print("{}".format( (str[i] + "\n") if (i == (l - 1)) else str[i]) , end="")
        i += 1
