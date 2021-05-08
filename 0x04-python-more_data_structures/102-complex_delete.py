#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys_del = []
        for key, content in a_dictionary.items():
            if content == value:
                keys_del.append(key)
        for key in keys_del:
            del a_dictionary[key]
    return a_dictionary
