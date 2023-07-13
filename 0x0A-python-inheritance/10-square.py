#!/usr/bin/python3
"""
Inherits from BaseGeometry
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    Params:
       size - reps the 4 sides of a square
    """

    def __init__(self, size):
        """Instantiating the private method square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns the area of the rectangle"""
        return (self.__size * self.__size)
