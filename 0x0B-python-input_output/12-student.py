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

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs and isinstance(attrs, list) and\
                all(isinstance(item, str) for item in attrs):
            dic = {}
            for key in attrs:
                if key in self.__dict__:
                    dic[key] = self.__dict__[key]
            return dic
        else:
            return self.__dict__
