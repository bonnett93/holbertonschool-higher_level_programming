#!/usr/bin/python3
'''File: 10 square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class Square, inheritance from Rectangle'''
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
