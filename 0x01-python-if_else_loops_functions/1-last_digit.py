#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ldigit = abs(number)
ldigit = ldigit % 10
if number < 0:
    ldigit *= -1
print("Last digit of", number, "is", ldigit, end="")
if ldigit > 5:
    print(" and is greater than 5")
if ldigit == 0:
    print(" and is 0")
if ldigit < 6 and ldigit != 0:
    print(" and is less than 6 and not 0")
