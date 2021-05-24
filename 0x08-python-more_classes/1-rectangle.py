#!/usr/bin/python3
"""The Module write a class Rectangle that defines a rectangle"""


class Rectangle:
    """A Class that deines a rectangle:
        -Instantiation with optional width and height:
            def __init__(self, width=0, height=0):
        -Private instance attribute: width:
            property def width(self): to retrieve it.
            property setter def width(self, value): to set it.
        -Private instance attribute: height:
            property def height(self): to retrieve it.
            property setter def height(self, value): to set it.
    """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__handle_error(value, 1)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__handle_error(1, value)
        self.__height = value

    def __handle_error(self, width, height):
        try:
            if type(width) != int or type(height) != int:
                raise TypeError
            elif width < 0 or height < 0:
                raise ValueError
        except TypeError:
            x = "width" if type(width) != int else "height"
            print("{} must be an integer".format(x), end="")
            raise
        except ValueError:
            x = "width" if width < 0 else "height"
            print("{} must be >= 0".format(x), end="")
            raise
