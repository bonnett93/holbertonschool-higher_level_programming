#!/usr/bin/python3
'''Module: base.py'''
import json


class Base:
    '''This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all other classes
    and to avoid duplicating the same code (by extension, same bugs)'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Class constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
