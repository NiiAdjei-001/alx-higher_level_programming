#!/usr/bin/python3
for r in range(0, 8):
    for c in range(0, 9):
        if r != c and c > r:
            print("{0}{1}".format(r, c), end=", ")
    print("{0}9".format(r), end=", ")
print("{}".format(89))
