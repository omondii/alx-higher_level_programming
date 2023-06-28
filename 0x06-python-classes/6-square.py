#!/usr/bin/python3
"""A square class
   Errors:
       TypeError accept int only. ValueError: int should > 0
   Returns: Prints a square with size dimentions
"""


class Square:
    """Defining a square with size as its argument"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if len(position) != 2 or not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise ValueError("position values must be >= 0")
        self.__position = position

    def area(self):
        """Calculates the area of a square.
           Args:
              __size (int): Dimensions of the square
        """
        return (self.__size) * (self.__size)

    def my_print(self):
        """public instance that prints in stdout with the character #"""
        for i in range(self.__size):
            if self.__size != 0:
                print("#" * self.__size)
            else:
                print()

    @property
    def size(self):
        """getter method: retrieves the size property"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter method: enforces type and value for the size arg"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """public instance that prints in stdout with the character #"""
        for i in range(self.__size):
            if self.__size != 0:
                print("#" * self.__size)
            else:
                print()
