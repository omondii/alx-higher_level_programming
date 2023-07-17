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

    def update(self, *args, **kwargs):
        """ Assign each argument to an attribute """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                if i == 1:
                    self.size = value
                if i == 2:
                    self.x = value
                if i == 3:
                    self.y = value

        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Pack and return a dictionary form square """
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
