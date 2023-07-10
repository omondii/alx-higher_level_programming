#!/usr/bin/pytho3
"""
Checks if an object is an instance of a class that inheritedfrom the specified
class. Directly or indirectly
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class that inherited (directly or
    indirectly) from the specified class ; otherwise False.
    Parameters:
        obj - objects
    Returns:
        If it is -True. If not -False
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
