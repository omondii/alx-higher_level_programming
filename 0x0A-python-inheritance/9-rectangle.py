#!/usr/bin/python3
"""
Inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGeometry
    Params:
        width - rectangle width
        height - rectangle height
    """
    def __init__(self, width, height):
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """returns formated string output to print()"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """returns the area of the rectangle"""
        return(self.__width * self.__height)
