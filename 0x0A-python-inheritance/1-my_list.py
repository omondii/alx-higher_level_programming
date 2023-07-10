#!/usr/bin/python3
"""
Class MyList that inherits from list
"""


class MyList(list):
    """
    A class that inherits from list
    Returns:
        A sorted list
    """
    def __init__(self):
        """public instance method"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
