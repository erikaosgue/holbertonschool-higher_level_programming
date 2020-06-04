#!/usr/bin/python3
"""
    11. Student to JSON
    module: 11-student.py
"""


class Student:
    """  class Student that defines a student by:
    Public instance attributes:
    first_name
    last_name
    age
    """

    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
