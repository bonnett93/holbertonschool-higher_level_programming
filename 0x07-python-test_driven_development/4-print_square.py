#!/usr/bin/python3
'''Module 4: print square'''


def print_square(size):
    '''prints a square with the character #.'''
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
        return
    for i in range(size):
        print("#"*size)
