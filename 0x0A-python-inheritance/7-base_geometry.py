#!/usr/bin/python3
'''File: 7 base geometry'''


class BaseGeometry:
    '''Base class BaseGeometry.'''
    def area(self):
        '''Area not implemented'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates value Type and Value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
