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
        """area A pulic instance method that returns
        the area of a square

        Returns:
            int: Area of the square
        """
        return (self.__size * self.__size)

    def __lt__(self, other):
        """__lt__ less than

        Function that compare two objects using less than

        Args:
            other (object): Is the area to the other member will be comparing

        Returns:
            [bool]: True
        """
        if self.area() < other.area():
            return True

    def __le__(self, other):
        """__le__ less or equal to

        Function that compare two objects using less or equal to

        Args:
            other (object): Is the area to the other member will be comparing

        Returns:
            [bool]: True
        """
        if self.area() <= other.area():
            return True

    def __eq__(self, other):
        """__eq__ equal

        Function that verifies if two objects have same area

        Args:
            other (object): Is the area to the other member will be comparing

        Returns:
            [bool]: True
        """
        if self.area() == other.area():
            return True

    def __gt__(self, other):
        """__gt__ less than

        Function that compare two objects using greater than

        Args:
            other (object): Is the area to the other member will be comparing

        Returns:
            [bool]: True
        """
        if self.area() > other.area():
            return True

    def __ge__(self, other):
        """__ge__ greater or equal to

        Function that compare two objects using >=

        Args:
            other (object): Is the area to the other member will be comparing

        Returns:
            [bool]: True
        """
        if self.area() >= other.area():
            return True

    def __ne__(self, other):
        """__ne__ not equal

        Function that checks if two objects are not equal

        Args:
            other (object): Is the area to the other member will be comparing

        Returns:
            [bool]: True
        """
        if self.area() != other.area():
            return True
