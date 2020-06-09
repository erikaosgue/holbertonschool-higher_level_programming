#!/usr/bin/python3
"""
    Unittest:  Rectangle Class
"""
import unittest
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle(unittest.TestCase):
    """Test Rectangle
    Args unittest.TestCase
    """

    def tearDown(self):
        Base.__nb_objects = 0

    def test_first_rectangle_datatype(self):
        """Test Rectangle Class"""

        # r1 = Rectangle(10, 2)
        # # self.assertEqual(r1.id, 10)
        # self.assertEqual(r1.id, 7)

        # r2 = Rectangle(2, 10)
        # # self.assertEqual(r2.id, 11)
        # self.assertEqual(r2.id, 8)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        with self.assertRaises(TypeError):
            Rectangle(1, None, 2)
            # TypeError: height must be an integer

        with self.assertRaises(TypeError):
            Rectangle("Hello", 2, 3)
            # TypeError: width must be an integer

        with self.assertRaises(ValueError):
            Rectangle(0, 0)
            # ValueError: width must be > 0

        with self.assertRaises(ValueError):
            Rectangle(-1, -4, 5, 2)
            # ValueError: width must be > 0

        with self.assertRaises(TypeError):
            Rectangle(1.2, 1.3, 1.4)
            # TypeError: width must be an integer

        with self.assertRaises(TypeError):
            Rectangle([1, 2], [3, 4])
            # TypeError: width must be an integer

        with self.assertRaises(TypeError):
            Rectangle({1, 2}, {3, 4})
            # TypeError: width must be an integer

        with self.assertRaises(TypeError):
            Rectangle({'A': 1})
            # TypeError: width must be an integer

        with self.assertRaises(TypeError):
            Rectangle([[1, 2], [3, 4]])
            # TypeError: width must be an integer

        with self.assertRaises(TypeError):
            Rectangle(True)
            # TypeError: width must be an integer

        with self.assertRaises(TypeError):
            Rectangle(1, 2, float('nan'), 2)
            # TypeError: x must be an integer

        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2)
            # TypeError: width must be an integer

        # only 1 arg
        with self.assertRaises(TypeError):
            Rectangle(1)
            # TypeError: __init__() missing 1 required positional argument: 'height'

        # too many args
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)
            # TypeError: __init__() takes from 3 to 6 positional arguments but 7 were given

    def test_validate_rectangle(self):

        with self.assertRaises(TypeError):
            Rectangle(10, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10

        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area_first(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display_0(self):

        r1 = Rectangle(4, 6)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "####\n####\n####\n####\n####\n####\n")

        r2 = Rectangle(2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), "##\n##\n")

    def test_str_(self):

        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] ({}) 2/1 - 4/6".format(r1.id))

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] ({}) 1/0 - 5/5".format(r2.id))

    def test_display_1(self):

        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

        r2 = Rectangle(3, 2, 1, 0)
        f = io.StringIO()
        with redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), " ###\n ###\n")

    def test_update_0(self):

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(
            str(r1), "[Rectangle] ({}) 10/10 - 10/10".format(r1.id))

        r1.update(89)
        self.assertEqual(
            str(r1), "[Rectangle] ({}) 10/10 - 10/10".format(r1.id))

        r1.update(89, 2)
        self.assertEqual(
            str(r1), "[Rectangle] ({}) 10/10 - 2/10".format(r1.id))

        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] ({}) 10/10 - 2/3".format(r1.id))

        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] ({}) 4/10 - 2/3".format(r1.id))

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] ({}) 4/5 - 2/3".format(r1.id))

    def test_update_1(self):

        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(
            str(r1), "[Rectangle] ({}) 10/10 - 10/10".format(r1.id))

        r1.update(height=1)
        self.assertEqual(
            str(r1), "[Rectangle] ({}) 10/10 - 10/1".format(r1.id))

        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] ({}) 2/10 - 1/1".format(r1.id))

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] ({}) 3/1 - 2/1".format(r1.id))

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] ({}) 1/3 - 4/2".format(r1.id))

    def test_rectangle_ins_to_dic_13(self):

        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(str(r1), "[Rectangle] ({}) 1/9 - 10/2".format(r1.id))
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(
            r1_dictionary, {'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10})

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] ({}) 1/9 - 10/2".format(r1.id))

        self.assertFalse(r1 == r2)
