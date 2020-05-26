#!/usr/bin/python3
"""
    5. Detect instance deletion
    Module: 5-rectangle.py
    Return: Information of the class
"""


class Rectangle:
    """
        defines a rectangle
        Methods:
            width, height, area, perimeter
            __str__, __repr__
    """

    def __init__(self, width=0, height=0):
        """
            Initializer
            Args:
                width (integer): Width if the rectangle.
                height (integer): height of the rectangle
        """
        self.width = width
        self.height = height

    # get the with
    @property
    def width(self):
        return self.__width

    # set the with
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        s = ""
        if self.perimeter() != 0:
            for i in range(self.height):
                for j in range(self.width):
                    s += "#"
                if i != self.height - 1:
                    s += "\n"
        return s

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
