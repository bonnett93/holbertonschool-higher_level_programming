#!/usr/bin/python3
'''File: 9 student'''


class Student:
    '''Class Student'''

    def __init__(self, first_name, last_name, age):
        '''Class Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''retrieves a dictionary representation of a Student instance'''
        return dict(self.__dict__)
