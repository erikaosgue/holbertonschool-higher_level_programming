#!/usr/bin/python3
"""
    12. Student to JSON with filter
    module: 12-student.py
"""


class Student:
    """  class Student that defines a student by:
    Public instance attributes:
    first_name
    last_name
    age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is not None) and type(attrs) is list and\
                all(type((item) is str) for item in attrs):
            dic = {}
            for key in attrs:
                if key in self.__dict__:
                    dic[key] = self.__dict__[key]
            return dic
        else:
            return self.__dict__
