#!/usr/bin/python3
def print_last_digit(number):
    ldigit = abs(number)
    ldigit = ldigit % 10
    print("{}".format(ldigit), end="")
    return ldigit
