#!/usr/bin/python3
"""
imported module
Base from models
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle inherits from Base
    Params: (pia->Private Instance attribute)
          width: width of the rectangle(pia)
          height: vertical length of the rect(pia)
          x - (pia)
          y - (pia)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize class rectangle with the class constructor
        for all atttributes
        super() allows allows us to access inherited methods
        """
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

        """
        each private attributes getter and setter. This allows us to protect
        class attributes and validate whatever we assign to a variable
        """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
