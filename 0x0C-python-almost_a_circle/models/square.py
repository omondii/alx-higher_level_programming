#!/usr/bin/python3
"""
Imported modules
from models, rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square inherits from rectangle
    initialize with self to obtain all rectangle methods
    params:
         same to Rectangle but size == width/height
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize the class. initialize rectangle using super """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str implemetation to unify output """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
