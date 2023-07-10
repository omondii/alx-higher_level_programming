#!/usr/bin/python3
"""
Checking obj type using type()
"""


def is_same_class(obj, a_class):
    """
    Function that check if an object is of the given class
    Parameters:
        obj - object whose class is to be checked
        a_class - Class to check for
    Returns:
        If is of same class -True else -False
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
