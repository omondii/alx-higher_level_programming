#!/usr/bin/python3
"""
No module used
"""
def lookup(obj):
    """
    function that returns the list of available attributes and methods of an
    object.
    Parameters:
         obj - object to get methods and atributes of
    Returns:
         A list
    """
    return dir(obj)
