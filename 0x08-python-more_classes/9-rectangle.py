#!/usr/bin/python3
"""Defines a rectangle

  Attributtes:
      width (int) - private instance to hold rectangle width
      height (int) - private instance to hold rectangle length
"""


class Rectangle:
    """
    Class rectangle represents a rectangle
    (Public) class attribute:
        number_of_instances - holds the number of object instances based on the
        init and del methods
        print_symbol - var to hold the print symbol that reps the object
         return[:1] -to remove the initial #
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle dimentions
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rectangle += str(self.print_symbol)
            rectangle += "\n"
        return rectangle[:-1]

    def __repr__(self):
        """returns a string rep of the rectangel.
        Can be used by eval to recreate
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Garbage collection method function. Prints a deletion
        notification
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Using a static method to compare the area of the 2 rectangle instances
        First check if both rect_1 and  2 are instances of rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

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

    @classmethod
    def square(cls, size=0):
        """
        A class method that returns a new rectangle instance
        """
        return cls(size,size)
