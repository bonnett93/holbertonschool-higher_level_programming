#!/usr/bin/python3
'''file: 2. append write'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file (UTF8)
    and returns the number of characters added:'''
    with open(filename, "a", encoding="UTF-8") as f:
        characters = f.write(text)
    return characters
