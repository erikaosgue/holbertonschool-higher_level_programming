#!/usr/bin/python3
"""
    Unittest Square class
"""
import unittest
import io
import pep8
from contextlib import redirect_stdout
from models.square import Square
from models.base import Base


class Test_Square(unittest.TestCase):
    """Test Square
    Args unittest.TestCase
    """

    def tearDown(self):
        """Function that updates the id"""
        Base.__nb_objects = 0

    def test_pep8_style(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
    def test_square(self):
        """Checks the datatype of the square """

        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        # display
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n#####\n#####\n")

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        # display
        f2 = io.StringIO()
        with redirect_stdout(f2):
            s2.display()
        self.assertEqual(f2.getvalue(), "  ##\n  ##\n")

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] ({}) 1/3 - 3".format(s3.id))
        self.assertEqual(s3.area(), 9)
        # display
        f3 = io.StringIO()
        with redirect_stdout(f3):
            s3.display()
        self.assertEqual(f3.getvalue(), "\n\n\n ###\n ###\n ###\n")

        with self.assertRaises(TypeError):
            s4 = Square()

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s5 = Square(1, [2], [3])

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s6 = Square(1, 2, -3)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s7 = Square(1, -2, -3)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s8 = Square(1, 2, [3])

        with self.assertRaises(TypeError):
            s9 = Square(1, 2, 3, 4, 5, 6)

    def test_square_size(self):
        """ Test for checking the size of the square """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] ({}) 0/0 - 5".format(s1.id))
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] ({:d}) 0/0 - 10".format(s1.id))

        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_square_update(self):
        """ Checks for the function Update"""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] ({}) 0/0 - 5".format(s1.id))

        s1.update(10)
        self.assertEqual(str(s1), "[Square] ({}) 0/0 - 5".format(s1.id))

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] ({}) 0/0 - 2".format(s1.id))

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] ({}) 3/0 - 2".format(s1.id))

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] ({}) 3/4 - 2".format(s1.id))

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] ({}) 12/4 - 2".format(s1.id))

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] ({}) 12/1 - 7".format(s1.id))

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] ({}) 12/1 - 7".format(s1.id))

    def test_square_ins_to_dic_14(self):
        """ Check for the instance transformation into a dict """

        s1 = Square(10, 2, 1)
        self.assertEqual(str(s1), "[Square] ({}) 2/1 - 10".format(s1.id))
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(
            s1_dictionary, {'id': s1.id, 'x': 2, 'size': 10, 'y': 1})

        s2 = Square(1, 1)
        self.assertEqual(str(s2), "[Square] ({}) 1/0 - 1".format(s2.id))
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), "[Square] ({}) 2/1 - 10".format(s2.id))
        self.assertFalse(s1 == s2)
