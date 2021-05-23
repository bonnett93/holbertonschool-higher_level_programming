#!/usr/bin/python3
"""Write a class Square that defines a square with size and area"""


class Square:
    """Create a class Square with:
        Private instance attribute:
            size
        Public instance method:
            def area(self)"""

    def __handle_error(self, size):
        """Check if the value of size is ok"""
        try:
            if type(size) != int:
                raise TypeError
            elif size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end="")
            raise
        except ValueError:
            print("size must be >= 0", end="")
            raise

    def __init__(self, size=0):
        """Init is the instantiated Class constructor"""
        self.__handle_error(size)
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size**2

    @property
    def size(self):
        """Retrieve value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size"""
        self.__handle_error(value)
        self.__size = value
