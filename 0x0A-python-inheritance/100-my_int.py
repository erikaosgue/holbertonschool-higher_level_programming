#!/usr/bin/python3
"""12. My integer"""


class MyInt(int):
    """ a class MyInt that inherits from int"""
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return not (self.number == other)

    def __ne__(self, other):
        return not (self.number != other)
