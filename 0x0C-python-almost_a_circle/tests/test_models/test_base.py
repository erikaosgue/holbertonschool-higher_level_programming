#!/usr/bin/python3
"""
    Unittest for 1. Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """Test Base
    Args unittest.TestCase
    """

    def tearDown(self):
        """Function that updates the id"""
        Base._Base__nb_objects = 0

    def test_base_datatype(self):
        """Test base"""

        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b6 = Base(None)
        self.assertEqual(b6.id, 3)
        b7 = Base("Hello")
        self.assertEqual(b7.id, "Hello")
        b8 = Base("")
        self.assertEqual(b8.id, "")
        b9 = Base(-1)
        self.assertEqual(b9.id, -1)
        b10 = Base(1.2)
        self.assertEqual(b10.id, 1.2)
        # ***
        with self.assertRaises(TypeError):
            b11 = Base(1, 2)
        b12 = Base([1, 2])
        self.assertEqual(b12.id, [1, 2])
        b13 = Base({1, 2})
        self.assertEqual(b13.id, {1, 2})
        b14 = Base({'A': 1})
        self.assertEqual(b14.id, {'A': 1})
        b15 = Base([[1, 2], [3, 4]])
        self.assertEqual(b15.id, [[1, 2], [3, 4]])
        b16 = Base(True)
        self.assertEqual(b16.id, True)
        b17 = Base(float('nan'))
        self.assertTrue(b17.id != b17.id)
        b18 = Base(float('inf'))
        self.assertEqual(b18.id, float('inf'))
        b19 = Base(float('-inf'))
        self.assertEqual(b19.id, float("-inf"))

    def test_dictionary_to_Json(self):
        """ Test Convert a Dictionary into a Json strin """

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary,
                         {'x': 2, 'width': 10, 'id': r1.id, 'height': 7, 'y': 8})

        # test list of dictionaries None
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary.__str__(), '[]')

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary.__str__(), '[]')

        json_dictionary = Base.to_json_string("Hello")
        self.assertEqual(json_dictionary.__str__(), '"Hello"')

        json_dictionary = Base.to_json_string([{}])
        self.assertEqual(json_dictionary, '[{}]')

        with self.assertRaises(TypeError):
            Base.to_json_string()

        with self.assertRaises(TypeError):
            Base.to_json_string(1, 2)

        json_dictionary = Base.to_json_string([{'1': 'True'}, {'2': 'False'}])
        self.assertEqual(json_dictionary.__str__(),
                         '[{"1": "True"}, {"2": "False"}]')

    def test_Json_string_to_file(self):
        """Test Save a Json String into a file"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))

        # Rectangle.save_to_file(None)

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        with self.assertRaises(TypeError):
            Rectangle.save_to_file(1, 2)

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("Hello")

        with self.assertRaises(AttributeError):
            Rectangle.save_to_file([1, "2", 2.3])

    def test_Json_string_to_dictionary(self):
        """test correct transformation from Json string to Dic"""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

    def test_dictionary_to_instance(self):
        """ test correct transormation from dictionary to Instance """

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 == r2)
        # check if dictionary is None
        r2 = Rectangle.create()

    def test_file_to_instances(self):
        """Test reading the file and transforming it into instances """

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.__str__(), list_rectangles_output[0].__str__())
        self.assertEqual(r2.__str__(), list_rectangles_output[1].__str__())


if __name__ == "__main__":
    unittest.main()
