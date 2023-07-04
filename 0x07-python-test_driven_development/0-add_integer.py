#!/usr/bin/python3
"""A function that adds two intergers"""

def add_integer(a, b=98):
    """
    Add two intergers and return the result.

    Parameters:
    a(float or int): First value to add
    b(float or int): Second value to add

    Returns:
    Sum of a and b: int
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance (b,(float, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
