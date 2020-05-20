#!/usr/bin/python3
"""Module that get the areaof a circunference"""
import math


class MagicClass:
    "Class that creates instance"

    def __init__(self, radius=0):
        "Constructor of MagicClass"
        self._MagicClass__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        "area of the circunference"
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        "Get the circunference "
        return 2 * math.pi * self._MagicClass__radius
