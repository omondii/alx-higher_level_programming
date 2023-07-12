#!/usr/bin/python3
"""
No module used
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file (UTF8) and returns the
    number of characters written.
    Params:
         filename: the name of the file to write
         text: the string to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
