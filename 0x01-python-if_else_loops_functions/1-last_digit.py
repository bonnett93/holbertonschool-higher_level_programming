#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = number % 10
if (number < 0):
    result = number % -10
print("Last digit of {} is ".format(number), end="")
if (result) > 5:
    print("{} and is greater than 5".format(result))
elif (result) == 0:
    print("{} and is 0".format(result))
else:
    print("{} and is less than 6 and not 0".format(result))
