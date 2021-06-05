#!/usr/bin/python3
'''Module 0: add_integer'''


def add_integer(a, b=98):
    '''Function that adds two numbers
        default value for b parameter is 98'''

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
