#!/usr/bin/python3
'''File: 8 class to json'''


def class_to_json(obj):
    '''Returns the dictionary description'''
    return dict(obj.__dict__)
