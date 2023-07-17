#!/usr/bin/python
"""
imported modules:
unittest
Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def setUp(self):
        """
        self.base1 = Base()
        self.base2 = Base()
        """

    def tearDown(self):
        """
        self.base1 = None
        self.base2 = None
        """

    def test_id_increment(self):
        """
            Test if the id is incrementing correctly
            assertEqual verifies if the returned value is similar
            to the expected one
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_initialization(self):
        """
        Test if id initializes correctly when given a value
        Id should be equal to value provided when calling base()
        """
        base = Base(10)
        self.assertEqual(base.id, 10)


if __name__ == '__main__':
    unittest.main()
