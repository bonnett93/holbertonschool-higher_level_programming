#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end="")

result = number % 10
if (number < 0):
    result = number % -10

if result < 6 and result != 0:
    print("{:d} and is less than 6 and not 0".format(result))
elif result == 0:
    print("{:d} and is 0".format(result))
else:
    print("{:d} and is greater than 5asdasd".format(result))
