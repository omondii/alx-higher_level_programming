#!/bin/usr/python3
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
        super().__init__()

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
