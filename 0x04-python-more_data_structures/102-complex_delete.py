#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        for key, content in a_dictionary.items():
            if content == value:
                del a_dictionary[key]
    return a_dictionary
