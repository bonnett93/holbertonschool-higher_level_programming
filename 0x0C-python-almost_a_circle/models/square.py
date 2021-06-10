#!/usr/bin/python3
'''Module: square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square Class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Class constructor'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Return size attribute'''
        return self.width

    @size.setter
    def size(self, value):
        '''Set size value'''
        self.width = value
        self.height = value

    def __str__(self):
        '''modify str method'''
        msg0 = "[Square] ({}) {}/{}".format(self.id, self.x, self.y)
        msg1 = " - {}".format(self.width)
        return msg0 + msg1

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        len_a = len(args)
        if len_a > 0:
            self.id = args[0]
            if len_a > 1:
                self.size = args[1]
                if len_a > 2:
                    self.x = args[2]
                    if len_a > 3:
                        self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                elif key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        diccionary = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
        return diccionary
