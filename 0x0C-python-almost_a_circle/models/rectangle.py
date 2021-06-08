#!/usr/bin/python3
'''Module: rectangle'''

from models.base import Base


class Rectangle(Base):
    '''Rectangle Class'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Class Constructor'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __setter_validator(self, name, value):
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if name in ['width', 'height']:
            if value <= 0:
                raise ValueError(name + " must be > 0")
        if name in ['x', 'y']:
            if value < 0:
                raise ValueError(name + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__setter_validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__setter_validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__setter_validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__setter_validator("y", value)
        self.__y = value
