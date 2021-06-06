#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""Class to test the max_integer function:
		This function find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
	def test_max_answer(self):
		'''Check if with the correct input, the result is ok'''
		# With positive integers
		self.assertAlmostEqual(max_integer([1,4,3,2,7]), 7)
		# With positive and negative integers
		self.assertAlmostEqual(max_integer([-1,4,3,-2,-7]), 4)
		# With integers and floats
		self.assertAlmostEqual(max_integer([1,4.5,3,2.2,7]), 7)
		# With empty list
		self.assertAlmostEqual(max_integer([]), None)
		# With negative integers
		self.assertAlmostEqual(max_integer([-2, -4, -6, -7]), -2)
		# With one element
		self.assertAlmostEqual(max_integer([12]), 12)
		# With one element
		self.assertAlmostEqual(max_integer([1, 3, 12, 5, 7]), 12)
