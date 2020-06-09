#!/usr/bin/python3
"""
    Unittest for 1. Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class Test_Base(unittest.TestCase):
    """Test Base
    Args unittest.TestCase
    """

    def tearDown(self):
        Base.__nb_objects = 0

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

        # b18 = Base(float('inf'))
        # self.assertEqual(b18.id, inf')

        # b19 = Base(float('-inf'))
        # self.assertEqual(b19.id, "-inf")

    def test_dictionary_to_Json(self):

        r1 = Rectangle(10, 7, 2, 8)

        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            dictionary, {'x': 2, 'width': 10, 'id': r1.id, 'height': 7, 'y': 8})

        # test list of dictionaries None
        json_dictionary = Base.to_json_string([])
        self.assertEqual(str(json_dictionary), '[]')

        json_dictionary = Base.to_json_string(None)
        self.assertEqual(str(json_dictionary), '[]')

    def test_Json_string_to_file(self):

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.isfile("Rectangle.json"))

        with open("Rectangle.json", "r", enconding="UTF-8") as file:
            self.assertCountEqual(str(file.read(
            )), '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
