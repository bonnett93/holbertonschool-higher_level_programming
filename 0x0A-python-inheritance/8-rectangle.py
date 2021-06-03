#!/usr/bin/python3
'''File: 8 Rectangle'''


class BaseGeometry:
    '''Base class BaseGeometry.'''
    def area(self):
        '''Area not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates value Type and Value'''
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''Class Rectangle, inheritance from BaseGeometry.'''
    def __init__(self, width, height):
        '''Class Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
