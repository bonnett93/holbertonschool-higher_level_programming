#!/usr/bin/python3
"""Write a class Square that defines a square with size and area"""


class Square:
    """Create a class Square with:
        -Instantiation:
            def __init__(self, size=0)
                -Private instance attribute:
                    size
                    position
        -Public instance method:
            def area(self)
            def my_print(self)
        -Getter
            def size(self):
            def position(self):
        -Setter
            def size(self, value)
            def position(self, value)"""

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

    def __handle_position(self, position=()):
        """Check if value of postition is ok"""
        a = position[0]
        b = position[1]
        try:
            if (a < 0 or b < 0 or len(position) != 2 or
               type(a) != int or type(b) != int):
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")
            raise

    def __init__(self, size=0, position=(0, 0)):
        """Init is the instantiated Class constructor"""
        self.__handle_error(size)
        self.__handle_position(position)
        self.__size = size
        self.__position = position

    def area(self):
        """Returns the current square area"""
        return self.__size**2

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print("")
            return
        for y in range(self.__position[1]):
                print("")
        for height in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for width in range(self.__size):
                print("#", end="")
            print("")

    @property
    def size(self):
        """Retrieve value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size"""
        self.__handle_error(value)
        self.__size = value

    @property
    def position(self):
        """Retrieve value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the value of position"""
        self.__handle_position(value)
        self.__position = value
