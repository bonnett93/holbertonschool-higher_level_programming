#!/usr/bin/python3
'''File: 11 student'''


class Student:
    '''Class Student'''

    def __init__(self, first_name, last_name, age):
        '''Class Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''retrieves a dictionary representation of a Student instance'''
        if attrs is None:
            return self.__dict__
        directory = {}
        if type(attrs) == list:
            for attr in attrs:
                if attr in self.__dict__:
                    directory[attr] = self.__dict__[attr]
        return directory

    def reload_from_json(self, json):
        if json is None:
            return
        for key, value in json.items():
            if key in self.__dict__:
                self.key = value
