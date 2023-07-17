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
    def setUp(self):
        """ Setup needed resources by creating rectangle instances"""
        self.r1 = Rectangle(10, 2, 5, 0)
        self.r2 = Rectangle(1, 3, 11, 15, 100)

    def tearDown(self):
        """ Clean up the resources used in the testsuite"""
        self.r1 = None
        self.r2 = None

    def test_initialization(self):
        """
        r1 && r2 test if the rectange is initalizing correctly for each
        instance
        We also check for the id value when passed and when not passed
        r1 - id is not passed
        r2 - id is passed
        """
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 5)
        self.assertEqual(self.r1.y, 0)

        """r2 instance. id=100"""
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r2.x, 11)
        self.assertEqual(self.r2.y, 15)
        self.assertEqual(self.r2.id, 100)

    def test_invalidtype(self):
        """ Test if the program raises type errors for non int input """
        with self.assertRaises(TypeError) as se:
            self.r3 = Rectangle("me", 4, 8, 16, 20)
        self.assertEqual(str(se.exception), "width must be an integer")

        with self.assertRaises(TypeError) as se:
            self.r4 = Rectangle(4, "5", 45, 7, 19)
        self.assertEqual(str(se.exception), "height must be an integer")

        with self.assertRaises(TypeError) as se:
            self.r5 = Rectangle(4, 5, "45", 7, 18)
        self.assertEqual(str(se.exception), "x must be an integer")

        with self.assertRaises(TypeError) as se:
            self.r6 = Rectangle(4, 5, 45, "7", 17)
        self.assertEqual(str(se.exception), "y must be an integer")

    def test_Invalidvalue(self):
        """ Test for errors for incorrect values """
        with self.assertRaises(ValueError) as se:
            self.r7 = Rectangle(-10, 6, 8, 15, 23)
        self.assertEqual(str(se.exception), "width must be > 0")

        with self.assertRaises(ValueError) as se:
            self.r8 = Rectangle(10, -6, 8, 15, 53)
        self.assertEqual(str(se.exception), "height must be > 0")

        with self.assertRaises(ValueError) as se:
            self.r9 = Rectangle(10, 6, -8, 15, 43)
        self.assertEqual(str(se.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as se:
            self.r10 = Rectangle(10, 6, 8, -15, 40)
        self.assertEqual(str(se.exception), "y must be >= 0")

class TestAreaDisplay(unittest.TestCase):
        """
        Test for the correct output
        Test for positive values, 0 values & negatives
        """
        def setUp(self):
            """ Setup needed resources by creating rectangle instances"""
            self.r3 = Rectangle(10, 5, id=34)
            self.r = Rectangle(10, 3, 6, 8, 56)
            self.rd = Rectangle(3, 2, id=10)

        def tearDown(self):
            """ Clean up the resources used in the testsuite"""
            self.r3 = None
            self.r  = None
            self.rd = None

        def test_area(self):
            result = self.r3.area()
            self.assertEqual(result, 50)

        def test_str(self):
            """ Test if the str method works as expected"""
            self.assertEqual(str(self.r), "[Rectangle] (56) 6/8 - 10/3")

        def test_display(self):
            """ Test if display gives expected shape """
            expected = "###\n###\n"
            with StringIO() as buffer, redirect_stdout(buffer):
                self.rd.display()
                result = buffer.getvalue()
            self.assertEqual(result, expected)

class TestUpdate(unittest.TestCase):
    def setUp(self):
        """ Setup needed resources by creating rectangle instances"""
        self.r = Rectangle(1, 1)

    def tearDown(self):
        """ Clean up the resources used in the testsuite"""
        self.r = None

    def test_arguments1(self):
        """
        Test if all attributes all updated correctly when empty/
        None/0 and argumets names are passed
        """
        r = Rectangle(1, 1)
        self.r.update(id=4, width=3, height=6, y=None)
        self.assertEqual(self.r.id, 3+1)
        self.assertEqual(self.r._Rectangle__width, 3)
        self.assertEqual(self.r._Rectangle__height, 6)
        self.assertEqual(self.r._Rectangle__x, 0)
        self.assertEqual(self.r._Rectangle__y, None)

    def test_arguments(self):
        """
        check if the attributes are correctly updated
        Test update with only values
        """
        r = Rectangle(1, 1)
        self.r.update(5, 10, 15, 20, 100)
        self.assertEqual(self.r.id, 5)
        self.assertEqual(self.r._Rectangle__width, 10)
        self.assertEqual(self.r._Rectangle__height, 15)
        self.assertEqual(self.r._Rectangle__x, 20)
        self.assertEqual(self.r._Rectangle__y, 100)


if __name__ == '__main__':
    unittest.main()
