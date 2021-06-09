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
        '''Validate if attribute is set correctly'''
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
        '''Return width value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width value'''
        self.__setter_validator("width", value)
        self.__width = value

    @property
    def height(self):
        '''Return height value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set height value'''
        self.__setter_validator("height", value)
        self.__height = value

    @property
    def x(self):
        '''Return x value'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set x value'''
        self.__setter_validator("x", value)
        self.__x = value

    @property
    def y(self):
        '''Return y value'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set y value'''
        self.__setter_validator("y", value)
        self.__y = value

    def area(self):
        '''Calculate and return the area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''prints in stdout the Rectangle instance with the character #'''
        if (self.__y != 0):
            print('\n' * (self.__y - 1))
        for row in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width))

    def __str__(self):
        '''change the str method'''
        msg1 = "[Rectangle] ({}) {}/{}".format(self.id, self.__x, self.__y)
        msg2 = " - {}/{}".format(self.__width, self.__height)
        return msg1 + msg2

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        len_a = len(args)
        if len_a > 0:
            self.id = args[0]
            if len_a > 1:
                self.__width = args[1]
                if len_a > 2:
                    self.__height = args[2]
                    if len_a > 3:
                        self.__x = args[3]
                        if len_a > 4:
                            self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__setter_validator("width", value)
                    self.__width = value
                if key == 'height':
                    self.__setter_validator("height", value)
                    self.__height = value
                if key == 'x':
                    self.__setter_validator("x", value)
                    self.__x = value
                if key == 'y':
                    self.__setter_validator("y", value)
                    self.__y = value

    def to_dictionary(self):
        '''returns the dictionary representation of a Rectangle'''
        diccionary = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
            }
        return diccionary
