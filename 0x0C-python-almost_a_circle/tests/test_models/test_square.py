#!/usr/bin/python3
'''Unittest for Square class'''
import unittest

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquate(unittest.TestCase):
    def setUp(self):
        '''Setup for instances = 0'''
        Base._Base__nb_objects = 0

    '''Class to test Square Class'''
    def testSquareInstance(self):
        '''Check instance creation and attributes'''
        # New instance, just one arguments
        s1 = Square(5)
        # Check id
        self.assertEqual(s1.id, 1)
        # Check height
        self.assertEqual(s1.height, 5)
        # Check width
        self.assertEqual(s1.width, 5)
        # Check x
        self.assertEqual(s1.x, 0)
        # Check y
        self.assertEqual(s1.y, 0)

        # New instance, all arguments
        s2 = Square(5, 5, 5, 5)
        # Check height
        self.assertEqual(s2.height, 5)
        # Check width
        self.assertEqual(s2.width, 5)
        # Check x
        self.assertEqual(s2.x, 5)
        # Check y
        self.assertEqual(s2.y, 5)
        # Check id
        self.assertEqual(s2.id, 5)
        # Check size
        self.assertEqual(s2.size, 5)

    def testSquareErrors(self):
        '''Check wrong instance creation and attributes'''
        # No arguments
        with self.assertRaises(TypeError):
            s = Square()
        # Wrong type argument height
        with self.assertRaises(TypeError):
            s = Square(10, "2")
        # Wrong value argument Width
        with self.assertRaises(ValueError):
            s3 = Square(10, 2)
            s3.size = -10
        # Wrong type argument x
        with self.assertRaises(TypeError):
            s4 = Square(10, 2)
            s4.x = {}
        # Wrong value argument y
        with self.assertRaises(ValueError):
            s = Square(10, 2, -3, 11)

    def test_str(self):
        '''Check instance method str'''
        s5 = Square(4)
        self.assertEqual(str(s5), "[Square] (1) 0/0 - 4")

    def test_size(self):
        '''Check size getter and setter'''
        s1 = Square(5)
        # checñ str
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        # check getter
        self.assertEqual(s1.size, 5)
        # chek setter
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        # error
        with self.assertRaises(TypeError):
            s1.size = "9"
        with self.assertRaises(ValueError):
            s1.size = -10

    def test_update_args(self):
        '''Check instance method update'''
        s1 = Square(10, 10, 10, 10)
        # No arguments
        s1.update()
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        # one argument
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")
        # two arguments
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")
        # three arguments
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")
        # four arguments
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")
        # five arguments

    def test_update_kwargs(self):
        '''Check instance method update'''
        s1 = Square(10, 10, 10, 10)
        # No arguments
        s1.update()
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        # if args existx, ignore kwargs
        s1.update(90, size=1)
        self.assertEqual(str(s1), "[Square] (90) 10/10 - 10")
        # one argument
        s1.update(size=1)
        self.assertEqual(str(s1), "[Square] (90) 10/10 - 1")
        # two arguments
        s1.update(size=1, x=2)
        self.assertEqual(str(s1), "[Square] (90) 2/10 - 1")
        # more arguments
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(str(s1), "[Square] (89) 3/1 - 2")
        # and more
        s1.update(x=1, size=2, y=3)
        self.assertEqual(str(s1), "[Square] (89) 1/3 - 2")
        # Type Error
        with self.assertRaises(TypeError):
            s1.update(x="12")
        # value error
        with self.assertRaises(ValueError):
            s1.update(size=-12)
