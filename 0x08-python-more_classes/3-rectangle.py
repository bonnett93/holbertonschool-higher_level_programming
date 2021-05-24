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
        """Instantiation Class constructor"""
        self.width = width
        self.height = height

    def __str__(self):
        """special method str"""
        if self.height == 0 or self.width == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += ('#' * self.width) + '\n'
            if (i == self.height - 1):
                return result[:-1]
        return result

    @property
    def width(self):
        """return width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Change width value"""
        self.__handle_error(value, 1)
        self.__width = value

    @property
    def height(self):
        """return height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """change height value"""
        self.__handle_error(1, value)
        self.__height = value

    def __handle_error(self, width, height):
        """Handle Errors"""
        if type(width) != int or type(height) != int:
            x = "width" if type(width) != int else "height"
            raise TypeError("{} must be an integer".format(x))
        elif width < 0 or height < 0:
            x = "width" if width < 0 else "height"
            raise ValueError("{} must be >= 0".format(x))

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return self.height * 2 + self.width * 2
