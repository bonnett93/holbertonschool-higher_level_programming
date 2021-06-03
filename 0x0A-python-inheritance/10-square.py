#!/usr/bin/python3
'''File: 10 square'''


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


class Rectangle(BaseGeometry):
    '''Class Rectangle, inheritance from BaseGeometry.'''
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method that return area of the Rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''Description of Rectangle'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    '''Class Square, inheritance from Rectangle'''
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
