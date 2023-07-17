#!/usr/bin/python3
"""
Imported modules;
unittest
Square
"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(10, 4, 6, 5)

    def tearDown(self):
        self.s1 = None
        self.s2 = None

    def test_initialization(self):
        self.assertEqual(self.s1.id, 5)
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s1.y, 6)
