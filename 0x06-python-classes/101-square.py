#!/usr/bin/python3
""" 6. Coordinates of a square """


class Square:
    """A class Square that defines a square by:
    Private instance attribute: size"""

    __size = 0
    __position = ()

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method to initialize an Instance

        Args:
            size (int): Number to be square
            position (Tuple): The position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position Getter

        Get the tuple with the position of the square

        Returns:
            Tuple: Contain the 2 coordanates (x and y)
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """position Setter

        Set Tuple with the position of the square

        Returns:
            Tuple: Contain the 2 coordanates (x and y)
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """area A pulic instance method that returns
        the area of a square

        Returns:
            int: Area of the square
        """
        return (self.__size * self.__size)

    def __str__(self):
        """my_print

        prints in stdout the square with the character #

        """
        s = ''
        if self.__size == 0:
            s += '\n'
        else:
            for y in range(self.__position[1]):
                s += '\n'
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    s += ' '
                for colum in range(self.__size):
                    s += '#'
                if (row != self.__size - 1):
                    s += '\n'
        return s
