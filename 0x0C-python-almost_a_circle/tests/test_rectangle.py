#!/usr/bin/python3
"""
imported modules:
unittest
Rectangle
"""
import unittest
from models.rectangle import Rectangle
from contextlib import redirect_stdout
from io import StringIO

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

class TestAreaDisplay(unittest.TestCase):
        """
        Test for the correct output
        Test for positive values, 0 values & negatives
        """
        def test_area(self):
            r3 = Rectangle(10, 5, id=34)
            result = r3.area()
            self.assertEqual(result, 50)

        def test_str(self):
            """ Test if the str method works as expected"""
            r = Rectangle(10, 3, 6, 8, 56)
            self.assertEqual(str(r), "[Rectangle] (56) 6/8 - 10/3")

        def test_display(self):
            """ Test if display gives expected shape """
            rd = Rectangle(3, 2, id=10)
            expected = "###\n###\n"
            with StringIO() as buffer, redirect_stdout(buffer):
                rd.display()
                result = buffer.getvalue()
            self.assertEqual(result, expected)

class TestUpdate(unittest.TestCase):
    def test_arguments1(self):
        """
        Test if all attributes all updated correctly when empty/
        None/0 and argumets names are passed
        """
        r = Rectangle(1, 1)
        r.update(id=4, width=3, height=6, y=None)
        self.assertEqual(r.id, 3+1)
        self.assertEqual(r._Rectangle__width, 3)
        self.assertEqual(r._Rectangle__height, 6)
        self.assertEqual(r._Rectangle__x, 0)
        self.assertEqual(r._Rectangle__y, None)

    def test_arguments(self):
        """
        check if the attributes are correctly updated
        Test update with only values
        """
        r4 = Rectangle(1, 1)
        r4.update(5, 10, 15, 20, 100)
        self.assertEqual(r4.id, 5)
        self.assertEqual(r4._Rectangle__width, 10)
        self.assertEqual(r4._Rectangle__height, 15)
        self.assertEqual(r4._Rectangle__x, 20)
        self.assertEqual(r4._Rectangle__y, 100)


if __name__ == '__main__':
    unittest.main()
