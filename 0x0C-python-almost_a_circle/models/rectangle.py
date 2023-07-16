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
        self.wh_checker("width", self.__width)
        self.wh_checker("height", self.__height)
        self.__x = x
        self.__y = y
        self.xy_checker("x", self.__x)
        self.xy_checker("y", self.__x)

    def wh_checker(self, name, value):
        """
        width & height checker. Must be of type int && not less than 0
        """
        if  not isinstance(value, int):
            raise TypeError(f"{name} must be an interger")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def xy_checker(self, name, value):
        """
        x and y checker. Must be of type int and not empty or less than 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an inerger")
        if value is None or value < 0:
            raise ValueError(f"{name} must be >= 0 ")

        """
        each private attributes getter and setter. This allows us to protect
        class attributes and validate whatever we assign to a variable
        """

    def area(self):
        """ Returns the area of each rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ prints # for every rectangle instance """
        for row in range(self.__height):
                print('#' * self.__width)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.wh_checker("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.wh_checker("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.xy_checker("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.xy_checker("y", value)
        self.__y = value
