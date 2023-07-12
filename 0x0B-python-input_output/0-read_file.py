#!/usr/bin/python3
"""
No module used
"""


def read_file(filename=""):
    """
    Function that reads a text file
    Params:
        filename: name of file to open
    """
    with open(filename, encoding="utf-8") as f:
        """
        basic open function to open a file
        """
        for line in f:
            print(line, end="")
