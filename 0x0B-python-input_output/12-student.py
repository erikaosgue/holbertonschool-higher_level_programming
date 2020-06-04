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

    def to_json(self, attrs=None):
        dic = {}
        if attrs:
            for key in attrs:
                if key in self.__dict__ and type(key) is str:
                    dic[key] = self.__dict__[key]
        else:
            return self.__dict__
        return dic
