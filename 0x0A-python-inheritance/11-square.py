#!/usr/bin/python3
'''File: 11 square'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class Square, inheritance from Rectangle'''
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)

    def __str__(self):
        '''Description of Rectangle'''
        return "[Square] {}/{}".format(self.__width, self.__height)
