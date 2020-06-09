#!/usr/bin/code
"""
    10. And now, the Square!
    models.square.py
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class that inherits from rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ calling the constructor of Rectangle to assing the values
            of rectangle """
        Rectangle.__init__(self, width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Return a string representation of the square """
        s = ""
        s += "[Square] ({}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
        return s

    @property
    def size(self):
        """The getter size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Verifies first the value before setting it """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the value atributes of the actual instance """
        if args and args is not ():
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ Dictionary representations of the instances """
        dic = {
            'x': self.x,
            'y': self.y,
            'size': self.size,
            'id': self.id
        }
        return dic
