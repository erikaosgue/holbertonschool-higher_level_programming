#!/usr/bin/python3
"""
    2. First Rectangle
    models/rectangle.py
"""
# Base = __import__('base').Base
# Base = __import__('base').Base
from .base import Base


class Rectangle(Base):
    """Rectangle Class that creates rectangles

    Args:
        Base (Super Class)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangles """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        # super().__init__(id)
        Base.__init__(self, id)

    @property
    def width(self):
        """width getter of the rectangles """
        return self.__width

    @width.setter
    def width(self, value):
        """ Verifies the value of width  and sets it """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ The gettter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """verifies the value of height and then sets it"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Coordenate of x position of the rectangle (getter)"""
        return self.__x

    @x.setter
    def x(self, value):
        """verifies the value for the x coordinate before seeting it """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ Its the getter for the y coordenate """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter of the y coordenate """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """DIsplay the rectangle using the # character """
        for y in range(self.__y):
            print()
        for i_row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j_colum in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Return a string representation of the rectangle """
        s = ""
        s += "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """Update the value atributes of the actual instance """
        if args and args is not ():
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.__width = value
                if key == 'height':
                    self.__height = value
                if key == 'x':
                    self.__x = value
                if key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """ Dictionary representations of the instances """
        # Two different ways to write dictionaries

        # dic = {}
        # dic['x'] = self.__x
        # dic['y'] = self.__y
        # dic['id'] = self.id
        # dic['height'] = self.__height
        # dic['width'] = self.__width
        dic = {
            'width': self.__width,
            'height': self.__height,
            'id': self.id,
            'x': self.__x,
            'y': self.__y
        }
        return dic
