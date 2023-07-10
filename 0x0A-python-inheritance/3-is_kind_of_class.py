#!/usr/bin/python3
"""
Checks if an object is an instance of a class that inherited
from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks is an object is an instance of a a given class
    Parameters:
       obj - object to check instance
       a_class - object class to check
    Returns:
       True if yes. False if not
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
