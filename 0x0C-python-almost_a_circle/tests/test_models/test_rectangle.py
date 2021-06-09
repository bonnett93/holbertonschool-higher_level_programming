#!/usr/bin/python3
'''Unittest for Rectangle class'''
import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    '''Class to test the Rectangle class'''

    def setUp(self):
        '''Setup for instances = 0'''
        Base._Base__nb_objects = 0

    def testRectangleInstance(self):
        '''Check instance creation and attributes'''
        # New instance, just two arguments
        r1 = Rectangle(5, 5)
        # Check id
        self.assertEqual(r1.id, 1)
        # Check height
        self.assertEqual(r1.height, 5)
        # Check width
        self.assertEqual(r1.width, 5)
        # Check x
        self.assertEqual(r1.x, 0)
        # Check y
        self.assertEqual(r1.y, 0)

        # New instance, all arguments
        r2 = Rectangle(5, 5, 5, 5, 5)
        # Check height
        self.assertEqual(r2.height, 5)
        # Check width
        self.assertEqual(r2.width, 5)
        # Check x
        self.assertEqual(r2.x, 5)
        # Check y
        self.assertEqual(r2.y, 5)
        # Check id
        self.assertEqual(r2.id, 5)

    def testRectangleErrors(self):
        '''Check wrong instance creation and attributes'''
        # No arguments
        with self.assertRaises(TypeError):
            r = Rectangle()
        # Wrong type argument height
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")
        # Wrong value argument Width
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        # Wrong type argument x
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        # Wrong value argument y
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 3, -1)

    def test_area(self):
        '''Check instance method area()'''
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        with self.assertRaises(TypeError):
            r3.area(8)

    def test_display(self):
        '''Check instance method display()'''
        # with No arguments
        r1 = Rectangle(4, 3)
        self.assertEqual(r1.display(), None)

        with self.assertRaises(TypeError):
            r1.display(4)

    def test_str(self):
        '''Check instance method str'''
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        '''Check instance method update'''
        r1 = Rectangle(10, 10, 10, 10)
        # No arguments
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        # one argument
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        # two arguments
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        # three arguments
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        # four arguments
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        # five arguments
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        '''Check instance method update'''
        r1 = Rectangle(10, 10, 10, 10, 10)
        # No arguments
        r1.update()
        self.assertEqual(str(r1), "[Rectangle] (10) 10/10 - 10/10")
        # if args existx, ignore kwargs
        r1.update(90, height=1)
        self.assertEqual(str(r1), "[Rectangle] (90) 10/10 - 10/10")
        # one argument
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (90) 10/10 - 10/1")
        # two arguments
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (90) 2/10 - 1/1")
        # more arguments
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        # and more
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")
        # Type Error
        with self.assertRaises(TypeError):
            r1.update(x="12")
        # value error
        with self.assertRaises(ValueError):
            r1.update(width=-12)
