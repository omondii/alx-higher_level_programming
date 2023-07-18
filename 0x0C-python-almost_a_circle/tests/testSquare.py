#!/usr/bin/python3
"""
Imported modules;
unittest
Square
"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.s1 = Square(10, 4, 6, 5)
        self.s2 = Square(8, 2)

    @classmethod
    def tearDown(self):
        del self.s1
        del self.s2

    def test_initialization(self):
        self.assertEqual(self.s1.id, 5)
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s1.y, 6)

        self.assertEqual(self.s2.size, 8)

    def test_typeerror(self):
        with self.assertRaises(TypeError) as se:
            s = Square("me")
        self.assertEqual(str(se.exception), "width must be an integer")

        with self.assertRaises(TypeError) as se:
            s = Square(1, "me", id=6)
        self.assertEqual(str(se.exception), "x must be an integer")

class TestUpdate(unittest.TestCase):
    def setUp(self):
        self.s1 = Square(1, 1, id=9)

    def tearDown(self):
        self.s1 = None

    def testSqArgs(self):
        self.s1.update(id=9, size=6, x=10, y=1)
        self.assertEqual(self.s1.id, 9)
        self.assertEqual(self.s1.size, 6)
        self.assertEqual(self.s1.x, 10)
        self.assertEqual(self.s1.y, 1 )
