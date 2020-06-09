#!/usr/bin/python3
"""
    1. Base class
    module: models/base.py
"""
import json
import csv
import turtle


class Base:
    """
        will be the “base” of all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constrictor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert from  dictionary to Json string """
        if list_dictionaries is None or list_dictionaries is {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Get the dictionaries of instances and converte them in Json
            strings, then will be save in a Json file"""
        filename = ""
        filename += str(cls.__name__) + ".json"
        with open(filename, 'w', encoding="utf-8") as file:
            # json_str = Base.to_json_string(list(map(lambda x: x.
            # to_dictionary(), list_objs)))
            list_dict = []
            if list_objs is None:
                file.write("[]")
            else:
                for instance in list_objs:
                    # list_dict = list_dict + [(instance.to_dictionary())]
                    # list_dict += [(instance.to_dictionary())]
                    list_dict.append(instance.to_dictionary())
                json_str = Base.to_json_string(list_dict)
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """convierte la Json string en un objeto (Dictionaries),
            luego en lista"""
        lista = []
        if json_string is None or "":
            return lista
        # here we are deserializing the string into an object
        obj = json.loads(json_string)
        # here we are converting the object (2 dictionaries)into a List
        return list(obj)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance base in the dictionary """
        if cls.__name__ == "Rectangle":
            x = cls(10, 10)
        elif cls.__name__ == "Square":
            x = cls(10)
        x.update(**dictionary)
        return x

    @classmethod
    def load_from_file(cls):
        """" Reads a file and convert from string to list of dictionaries
        then will be created a list of instances"""
        list_of_instances = []
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                file_str = file.read()
                list_of_dictionaries = Base.from_json_string(file_str)
                for dictionary in list_of_dictionaries:
                    list_of_instances += [cls.create(**dictionary)]
            return list_of_instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Transform a list of intances in a cvs file using its dictionaries"""
        filename = ""
        filename += str(cls.__name__) + ".csv"
        with open(filename, 'w', newline='', encoding="utf-8") as csv_file:
            list_dict = []
            for instance in list_objs:
                list_dict.append(instance.to_dictionary())

            # converting the list of dictionaries, in csv format
            keys = list_dict[0].keys()
            dict_writer = csv.DictWriter(csv_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """ Read the cvs file to transform in object dictionaries, and then in a
        list of instances"""
        filename = ""
        filename += str(cls.__name__) + ".csv"
        try:
            list_of_dictionaries = []
            with open(filename, 'r', newline='', encoding="utf-8") as csv_file:

                # converting from csv format dict to list of dictionaries
                list_of_dictionaries = [
                    {k: int(v) for k, v in row.items()}
                    for row in csv.DictReader(csv_file, skipinitialspace=True)]

                # creating the new instances with the dictionaries
                list_of_instances = []
                for dictionary in list_of_dictionaries:
                    list_of_instances += [cls.create(**dictionary)]
            return list_of_instances
        except FileNotFoundError:
            return []
