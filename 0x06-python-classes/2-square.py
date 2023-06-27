#!/usr/bin/python3
""" Defines a square with a given size.
    size must be an of type int and greater than or equal to 0.

    Attributes:
        __size (int): The size of the square
"""


class Square:
    """Defining a square with size as its argument"""
    def __init__(self, size=0):
        """Initializing the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
