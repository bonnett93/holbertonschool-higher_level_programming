#!/usr/bin/python3
"""Write a class Square that defines a square with size."""


class Square:
    """Create a class Square with:
        Private instance attribute: size"""

    def __init__(self, size = 0):
        """Init is the instantiated Class constructor"""
        try:
            if type(size) != int:
                raise TypeError
            elif size < 0:
                raise ValueError
            else:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
