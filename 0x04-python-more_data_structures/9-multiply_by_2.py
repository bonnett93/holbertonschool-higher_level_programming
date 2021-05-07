#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for key, value in a_dictionary.items():
        new_dic[key] = value * 2
    return new_dic
