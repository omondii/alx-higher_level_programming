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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        """
        each private attributes getter and setter. This allows us to protect
        class attributes and validate whatever we assign to a variable
        """

    def area(self):
        """ Returns the area of each rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ prints # for every rectangle instance """
        for _ in range(self.__y):
            print()
        for row in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            print('#' * self.__width)

    def __str__(self):
        """ __str__ implementation """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """ Public method tahta assigns an argument to each attribute """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    self.id = value
                if i == 1:
                    self.__width = value
                if i == 2:
                    self.__height = value
                if i == 3:
                    self.__x = value
                if i == 4:
                    self.__y = value
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """ Pack and return rectangle instances into dictionary """
        return {"id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
