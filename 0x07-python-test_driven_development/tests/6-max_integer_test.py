#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unittest to check the function """
    def test_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 4, 2, 1]), 4)
        self.assertEqual(max_integer([-2, -6, -3, -10]), -2)
        self.assertEqual(max_integer([4]), 4)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([5.60, 1, 3.8, 4]), 5.60)
        self.assertEqual(max_integer([5.23, 2.999, 3.6, 6.4778]), 6.4778)

    def test_string(self):
        self.assertEqual(max_integer(["Software", "Engineer"]), 'Engineer')
        self.assertEqual(max_integer("software"), 't')
