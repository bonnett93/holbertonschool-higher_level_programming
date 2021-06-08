#!/usr/bin/python3
'''Unittest for Rectangle class'''
import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    '''Class to test the Rectangle class'''

    def testRectangleInstance(self):
        '''Check instance creation and attributes'''
        # New instance, just two arguments
        r1 = Rectangle(5, 5)
        # Check id
        self.assertEqual(r1.id, 3)
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
