#!/usr/bin/python3
"""1- Square with size """


class Square:
    """A class Square that defines a square by size"""
    __size = 0

    def __init__(self, size):
        """__init__ method to initialize an Instance
        size (int): Number to be square
        """
        self.__size = size
