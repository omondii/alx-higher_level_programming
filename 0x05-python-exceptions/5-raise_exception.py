#!/usr/bin/python3
"""
raise_exception - raises a  type exception
"""


def raise_exception():
    try:
        raise TypeError("Type exception raised")
    except TypeError as e:
        raise e
