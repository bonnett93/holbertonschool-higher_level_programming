#!/usr/bin/python3
'''Unittest for Base class'''
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    '''Class to test the Base class
    '''
    def test_base_output(self):
        '''Check if a Base instance is created correctly'''
        # Create instance with no argument
        b1 = Base()
        # check if b1 is instances o Base
        self.assertIsInstance(b1, Base)

        self.assertEqual(b1.id, 1)

        # Create instance with no argument for second time
        b2 = Base()
        self.assertEqual(b2.id, 2)

        # Create instance with an argument
        b3 = Base(54)
        self.assertEqual(b3.id, 54)

        # Create instance with an argument for second time
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

        # Create instance with no argument and check the consecutive id
        b5 = Base()
        self.assertEqual(b5.id, 3)

        # Create instance with more arguments, Expectec error
        with self.assertRaises(TypeError):
            b = Base(12, 54)
