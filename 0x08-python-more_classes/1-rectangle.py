#!/usr/bin/python3
"""
    Module: 1. Real definition of a rectangle
    class Rectangle: Defines a rectangle

"""


class Rectangle:
    """
        defines a rectangle
        empty class
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
