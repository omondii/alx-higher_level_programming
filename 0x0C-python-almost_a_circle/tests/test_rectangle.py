#!/usr/bin/python3
"""
imported modules:
unittest
Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        """
        r1 && r2 test if the rectange is initalizing correctly for each
        instance
        We also check for the id value when passed and when not passed
        r1 - id is not passed
        r2 - id is passed
        """
        r1 = Rectangle(10, 2, 5, 0)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(1, 3, 11, 15, 100)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 11)
        self.assertEqual(r2.y, 15)
        self.assertEqual(r2.id, 100)

    def test_invalidtype(self):
        """ Test if the program raises type errors for non int input """
        with self.assertRaises(TypeError):
            Rectangle("me")

    def test_invalidvalue(self):
        """ Test if the program raises value error for less than 0
        width & height"""
        with self.assertRaises(ValueError):
            Rectangle(-1, -10)

    def test_invalid_xyvalue(self):
        """ Test if the prog raises value error for non positive
        numbers x&y """
        with self.assertRaises(ValueError):
            Rectangle(1, 4, -1)

class TestArea(unittest.TestCase):
        """
        Test for the correct output
        Test for positive values, 0 values & negatives
        """
        def test_area(self):
            r3= Rectangle(10, 5, id=34)
            result = r3.area()
            self.assertEqual(result, 50)



if __name__ == '__main__':
    unittest.main()
