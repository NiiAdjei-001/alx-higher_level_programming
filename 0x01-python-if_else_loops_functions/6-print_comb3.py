#!/usr/bin/python3
for r in range(0, 8):
    for c in range(0, 9):
        if r != c and c > r:
            print(f"{r}{c}", end=", ")
    print(f"{r}9", end=", ")
print("89")
