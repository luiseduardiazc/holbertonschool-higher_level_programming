#!/usr/bin/python3
""" Test for class Base """
import unittest
import json
from unittest import mock
import pep8
from io import StringIO
import inspect
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangleDocumentation(unittest.TestCase):
    """ calss to check documentation for Base class """

    @classmethod
    def setUpClass(cls):
        """ This method run before all test and
            find into Base class all functions.
            it store in a list of tuples """
        cls.list_rectangle_functions = inspect.getmembers(
            Rectangle, inspect.isfunction)

    def test_pep8_regtangle_class(self):
        """ Test that models/rectangle.py conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in rectangle.py")

    def test_pep8_rectangle_test(self):
        """ Test that test/test_models/test_rectangle.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_regtangle.py")

    def test_module_documentation(self):
        """ check module documentation """
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_documentation(self):
        """ check class Base documentation """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_functions(self):
        """ check documentation for every function """
        for item in self.list_rectangle_functions:
            function = item[1]
            self.assertTrue(len(function.__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ reset Base class attribute """
        Base._Base__nb_objects = 0
        cls.rect1 = Rectangle(width=20, height=2, x=5, y=6, id=20)
        cls.rect2 = Rectangle(width=1, height=100, x=7, y=50, id=7)
        cls.rect3 = Rectangle(width=25, height=14, x=47, y=10, id=7)
        cls.rect4 = Rectangle(width=2, height=8, x=78, y=98, id=21)

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_width(self):
        """test width """
        self.assertEqual(self.rect1.width, 20)
        self.assertEqual(self.rect2.width, 1)
        self.assertEqual(self.rect3.width, 25)
        self.assertEqual(self.rect4.width, 2)

    def test_height(self):
        """test height """
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect2.height, 100)
        self.assertEqual(self.rect3.height, 14)
        self.assertEqual(self.rect4.height, 8)

    def test_x(self):
        """test x """
        self.assertEqual(self.rect1.x, 5)
        self.assertEqual(self.rect2.x, 7)
        self.assertEqual(self.rect3.x, 47)
        self.assertEqual(self.rect4.x, 78)

    def test_y(self):
        """test y """
        self.assertEqual(self.rect1.y, 6)
        self.assertEqual(self.rect2.y, 50)
        self.assertEqual(self.rect3.y, 10)
        self.assertEqual(self.rect4.y, 98)

    def test_id(self):
        """test y """
        self.assertEqual(self.rect1.id, 20)
        self.assertEqual(self.rect2.id, 7)
        self.assertEqual(self.rect3.id, 7)
        self.assertEqual(self.rect4.id, 21)

    def test_mandatory_arguments(self):
        with self.assertRaises(TypeError):
            self.rect1 = Rectangle()

    def test_mandatory_width(self):
        with self.assertRaises(TypeError):
            self.rect1 = Rectangle(height=50, x=5, y=6, id=20)

    def test_mandatory_height(self):
        with self.assertRaises(TypeError):
            self.rect1 = Rectangle(width=20, x=5, y=6, id=20)

    def test_width_TypeError(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle("Test", 50, id=20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect1 = Rectangle(False, 50, id=20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect2 = Rectangle(None, 50, id=20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect3 = Rectangle([], 50, id=20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect4 = Rectangle({10}, 50, id=20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect2 = Rectangle(object, 50, id=20)

    def test_height_TypeError(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(10, "Test", 50, id=20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect1 = Rectangle(10, False, 50, id=20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect2 = Rectangle(10, None, 50, id=20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect3 = Rectangle(10, [], 50, id=20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect4 = Rectangle(10, {10}, 50, id=20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect2 = Rectangle(10, object, 50, id=20)

    def test_x_TypeError(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(10, 20, "TEST", id=20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect1 = Rectangle(10, 20, True, id=20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect2 = Rectangle(10, 40, None, id=20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect3 = Rectangle(10, 5, [], id=20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect4 = Rectangle(10, 10, {}, id=20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect2 = Rectangle(10, 5, Rectangle, id=20)

    def test_y_TypeError(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(10, 20, 20, "", id=20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect1 = Rectangle(10, 20, 2, None,  id=20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect2 = Rectangle(10, 40, 5, [],  id=20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect3 = Rectangle(10, 5, 8, [[]],  id=20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect4 = Rectangle(10, 10, 8, {}, id=20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect2 = Rectangle(10, 5, 7, Rectangle,  id=20)

    def test_width_ValueError(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(0, 50, id=20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect1 = Rectangle(-1, 50, id=20)

    def test_height_ValueError(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(50, 0, id=20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect1 = Rectangle(20, -10, id=20)

    def test_x_ValueError(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect = Rectangle(50, 45, -80, id=20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect1 = Rectangle(20, 4, -5, id=20)

    def test_y_ValueError(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect = Rectangle(50, 45, 80, -85, id=20)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect1 = Rectangle(20, 4, 5, -7, id=20)

    def test_id_instances(self):
        Base._Base__nb_objects = 0
        rect1 = Rectangle(width=20, height=2, x=5, y=6)
        rect2 = Rectangle(width=1, height=100, x=7, y=50)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)

    def test_area(self):
        r1 = Rectangle(5, 2)
        r2 = Rectangle(3, 8)
        self.assertEqual(r1.area(), 10)
        self.assertEqual(r2.area(), 24)

    def test_area_arguments(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(50, 10, 8)
            r1.area(10, 50)

    def test_display_arguments(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(50, 10, "")
            r1.display(10)

    def test_display_simple(self):
        """ Mock documentation
            https://docs.python.org/3/library/unittest.mock.html

            https://github.com/mikec964/chelmbigstock/wiki/
            Testing-printed-output-in-Python-2-and-Python-3
        """
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 6)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            r1.display()
            output = std_out.getvalue()
            self.assertEqual(output, ("#" * 4 + "\n") * 6)
        with mock.patch('sys.stdout', new=StringIO()) as std_out:
            r2.display()
            output = std_out.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 6)

    def test_display_complex(self):
        r1 = Rectangle(2, 3, 2, 2)
        r2 = Rectangle(3, 2, 1, 0)
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

    def test_str_method(self):
        r1 = Rectangle(20, 5)
        r2 = Rectangle(21, 5, 3)
        self.assertEqual(str(self.rect1), "[Rectangle] (20) 5/6 - 20/2")
        self.assertEqual(str(self.rect2), "[Rectangle] (7) 7/50 - 1/100")
        self.assertEqual(str(self.rect3), "[Rectangle] (7) 47/10 - 25/14")
        self.assertEqual(str(self.rect4), "[Rectangle] (21) 78/98 - 2/8")

        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 20/5")
        self.assertEqual(str(r2), "[Rectangle] (2) 3/0 - 21/5")

    def test_update_arguments(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(20)
        self.assertEqual(str(r1), "[Rectangle] (20) 10/10 - 10/10")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/10")
        r1.update(5, 50, y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (5) 3/1 - 50/10")

    def test_update_width_TypeError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, "TEST")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(5, width="###")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(10, "###", width=5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.update(8, [])

    def test_update_height_TypeError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, "")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, [{}])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r1.update(1, 2, height="test")

    def test_update_x_TypeError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 5, 8, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r1.update(1, 5, 8, x={})

    def test_update_y_TypeError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 8, 20, 78, False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r1.update(1, 8, 20, y=[8])

    def test_update_width_ValueError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(10, -5)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r1.update(10, width=-8)

    def test_update_height_ValueError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(1, 50, -45)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r1.update(1, 50,  height=-100)

    def test_update_x_ValueError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(5, 5, 7, -50)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r1.update(5, 5, 7, x=-10)

    def test_update_y_ValueError(self):
        r1 = Rectangle(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(5, 7, 8, 8, -8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r1.update(5, 7, 8, 8,  y=-50)

    def test_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        dic = r1.to_dictionary()
        self.assertDictEqual(
            dic, {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        r2 = Rectangle(10, 2, 20, 8)
        dic = r2.to_dictionary()
        self.assertTrue(dict, dic)
        self.assertDictEqual(
            dic, {'x': 20, 'y': 8, 'id': 2, 'height': 2, 'width': 10})

    def test_to_dictionary_noequal(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(10, 2, 1, 9)
        self.assertNotEqual(r1, r2)

    def test_update_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        dic = r1.to_dictionary()
        r2 = Rectangle(8, 20, 5, 1)
        r2.update(**dic)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)
        self.assertListEqual(json.loads(json_dictionary), [
            {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}])
        json_dictionary = Base.to_json_string("")
        self.assertEqual(json_dictionary, '""')
        json_dictionary = Base.to_json_string("test")
        self.assertEqual(json_dictionary, '"test"')
        json_dictionary = Base.to_json_string(True)
        self.assertEqual(json_dictionary, "true")
        json_dictionary = Base.to_json_string([{'id': 50}, {'test': 'test'}])
        self.assertListEqual(json.loads(json_dictionary), [
                             {"id": 50}, {"test": "test"}])

    def test_to_json_string_empty(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Rectangle.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_TypeError(self):
        r1 = Rectangle(10, 7, 2, 8)
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string()
        with self.assertRaises(TypeError):
            json_dictionary = Base.to_json_string([], [])

    def test_save_to_file(self):
        pass

    def test_from_json_string_empty(self):
        list_output = Rectangle.from_json_string([])
        self.assertListEqual(list_output, [])
        list_output = Rectangle.from_json_string(None)
        self.assertListEqual(list_output, [])

    def test_from_json_string(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertListEqual(list_output, [
            {'height': 4, 'width': 10, 'id': 89},
            {'height': 7, 'width': 1, 'id': 7}
        ])

    def test_from_json_string_TypeError(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        with self.assertRaises(TypeError):
            list_output = Rectangle.from_json_string()


if __name__ == "__main__":
    unittest.main()
