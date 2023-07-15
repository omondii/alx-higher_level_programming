#!/usr/bin/python3
"""
No imported modules
"""


class Base:
    """
    This is the base class of of all other classes in this project
    base.py manages id attribute in all future classes.
    Params:
         private class attribute: __nb_objects
         id: increments according to the public attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
