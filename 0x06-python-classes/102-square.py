#!/usr/bin/python3
""" 102. Compare 2 squares"""


class Square:
    """A class Square that defines a square by:
    Private instance attribute: size"""
    __size = 0

    def __init__(self, size=0):
        """__init__ method to initialize an Instance

        Args:
            size (int, optional): [description]. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """size getter

        Get size  value

        Returns:
            integer: size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size Setter

        Checks if the value is an Integer and positive

        Args:
            Set size  value
        """

        if isinstance(value, int):
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
        else:
            raise TypeError('size must be an integer')

    def area(self):
        return (self.__size * self.__size)

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()
