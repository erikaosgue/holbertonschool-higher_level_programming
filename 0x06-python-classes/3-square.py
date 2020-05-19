#!/usr/bin/python3
""" 2. Size validation"""


class Square:
    """A class Square that defines a square by:
    Private instance attribute: size"""
    __size = 0

    def __init__(self, size=0):
        """__init__ method to initialize an Instance
        Args:
            size (int): Number to be square
        """
        self.__size = size
        if isinstance(self.__size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """area A pulic instance method that returns
        the area of a square
        Returns:
            int: Area of the square
        """
        return (self.__size * self.__size)
