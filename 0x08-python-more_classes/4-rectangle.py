#!/usr/bin/python3
"""Defines a rectangle

  Attributtes:
      width (int) - private instance to hold rectangle width
      height (int) - private instance to hold rectangle length
"""


class Rectangle:
    """
    Class rectangle represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle dimentions
        """
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        try:
            return (self.__width + self.__height) * 2
        except self.__width == 0 or self.__heigth == 0:
            return 0

    def __str__(self):
        """implementing str method to unify the rectangle formating
           Parameters:
                   Rectangle: holds the shape of the rectangle
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += "#"
            rectangle += "\n"
        return rectangle


    @property
    def width(self):
        """Getter method. Sets the current value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width == Value"""
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method. Sets the current height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter: will set height to Value"""
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
