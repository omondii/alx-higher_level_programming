#!/usr/bin/python3
"""
No module used
"""


def append_write(filename="", text=""):
    """
    A function that appends a string at the end of a text file
    params:
       filename: name of the file to append
       text: the string to append
    Return:
       Number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        """
        append text to the end of a file
        "a" - append
        """
        f.write(text)
        return len(text)
