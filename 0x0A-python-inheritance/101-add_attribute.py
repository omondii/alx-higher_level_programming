#!/usr/bin/python3
"""
No modules imported
"""


def add_attribute(obj, attr_name, attr_value):
    """
    Function that adds a new attribute to an object if possible.
    Params:
        obj: The object to add the attribute to.
        attr_name: The name of the attribute to add.
        attr_value: The value of the attribute to add.
    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
