#!/usr/bin/python3
""" Test for class Base """
import unittest
from unittest import mock
import pep8
from io import StringIO
import inspect
from models import square
from models.base import Base
Square = square.Square


class TestSquareDocumentation(unittest.TestCase):
    """ calss to check documentation for Base class """

    @classmethod
    def setUpClass(cls):
        """ This method run before all test and
            find into Base class all functions.
            it store in a list of tuples """
        cls.list_square_functions = inspect.getmembers(
            Square, inspect.isfunction)

    def test_pep8_square_class(self):
        """ Test that models/square.py conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_square.py")

    def test_pep8_square_test(self):
        """ Test that test/test_models/test_square.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_square.py")

    def test_module_documentation(self):
        """ check module documentation """
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_documentation(self):
        """ check class Base documentation """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_functions(self):
        """ check documentation for every function """
        for item in self.list_square_functions:
            function = item[1]
            self.assertTrue(len(function.__doc__) >= 1)


class TestSquared(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_instances(self):
        s1 = Square(size=20, x=30, y=12)
        s2 = Square(size=25, x=5, y=8)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_size(self):
        """ test size """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 20
        self.assertEqual(s1.size, 20)

    def test_mandatory_size(self):
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_size_TypeError(self):
        s1 = Square(20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = ""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square("test")

    def test_x_TypeError(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(20, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(20, [])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(20, "###")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(20, {})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1 = Square(20, Square)

    def test_y_TypeError(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(20, 10, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(20, 4, [])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(20, 5, "###")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(20, 8, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1 = Square(20, 5, Square)

    def test_size_ValueError(self):
        s1 = Square(20, 5, 30)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s2 = Square(-20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -8

    def test_x_ValueError(self):
        s1 = Square(20, 10, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s2 = Square(20, -10, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.x = -50

    def test_y_ValueError(self):
        s1 = Square(20, 10, 8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s2 = Square(20, 10, -8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.y = -50

    def test_area(self):
        s1 = Square(20, 10, 8)
        s2 = Square(5, 5, 2)
        self.assertEqual(s1.area(), 400)
        self.assertEqual(s2.area(), 25)

    def test_area_arguments(self):
        with self.assertRaises(TypeError):
            s1 = Square(20, 10, 8)
            s1.area(10, 50)

    def test_str_method(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")

    def test_display_simple(self):
        """ Mock documentation
            https://docs.python.org/3/library/unittest.mock.html

            https://github.com/mikec964/chelmbigstock/wiki/
            Testing-printed-output-in-Python-2-and-Python-3
        """
        s1 = Square(5)
        s2 = Square(2)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            s1.display()
            output = std_out.getvalue()
            self.assertEqual(output, ("#" * s1.width + "\n") * s1.height)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            s2.display()
            output = std_out.getvalue()
            self.assertEqual(output, ("#" * s2.width + "\n") * s2.height)

    def test_display_complex(self):
        r1 = Square(2, 2)
        r2 = Square(3, 1, 3)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            r1.display()
            output = std_out.getvalue()
            coord_y = "\n" * r1.y
            string = "\n".join(((" " * r1.x) + ("#" * r1.width))
                               for i in range(r1.height))
            expected = coord_y + string + "\n"
            self.assertEqual(output, expected)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            r2.display()
            output = std_out.getvalue()
            coord_y = "\n" * r2.y
            string = "\n".join(((" " * r2.x) + ("#" * r2.width))
                               for i in range(r2.height))
            expected = coord_y + string + "\n"
            self.assertEqual(output, expected)

    def test_size_str(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.size = "9"

    def test_update_arguments(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s1.update(20)
        self.assertEqual(str(s1), "[Square] (20) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 0/1 - 7")
        s1.update(10, 50, size=7, id=89, x=1, y=3)
        self.assertEqual(str(s1), "[Square] (10) 1/3 - 50")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 1/1 - 7")

    def test_update_size_TypeError(self):
        s1 = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(10, "&&&")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(5, size="###")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(10, size=[])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1.update(8, None)

    def test_update_x_TypeError(self):
        s1 = Square(5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(1, 5, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.update(1, 5, x={})

    def test_update_y_TypeError(self):
        s1 = Square(20, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(1, 8, 20, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.update(1, 8, y=[8])

    def test_update_size_ValueError(self):
        s1 = Square(20, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(10, -5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.update(10, size=-8)

    def test_update_x_ValueError(self):
        s1 = Square(20, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(5, 5, -50)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s1.update(5, 5,  x=-10)

    def test_update_y_ValueError(self):
        s1 = Square(20, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(5, 7, 8, -8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s1.update(5, 7, 8, y=-50)

    def test_to_dictionary(self):
        s1 = Square(10, 2, 1)
        dic = s1.to_dictionary()
        self.assertDictEqual(dic, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        s2 = Square(1, 1)
        dic = s2.to_dictionary()
        self.assertTrue(dict, dic)
        self.assertDictEqual(dic, {'id': 2, 'x': 1, 'size': 1, 'y': 0})

    def test_to_dictionary_noequal(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        self.assertNotEqual(s1, s2)

    def test_update_to_dictionary(self):
        s1 = Square(10, 2, 1)
        dic = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**dic)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
