#!/usr/bin/python3
""" Test for class Base """
import unittest
import pep8
import inspect
from models import base
Base = base.Base


class TestBaseDoc(unittest.TestCase):
    """ calss to check documentation for Base class """

    @classmethod
    def setUpClass(cls):
        """ This method run before all test and
            find into Base class all functions.
            it store in a list of tuples """
        cls.list_base_functions = inspect.getmembers(Base, inspect.isfunction)

    def test_pep8_base_class(self):
        """ Test that models/base.py conforms to PEP8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_base.py")

    def test_pep8_base_test(self):
        """ Test that test/test_models/test_base.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found pep8 erros and warnings in test_base.py")

    def test_module_documentation(self):
        """ check module documentation """
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_documentation(self):
        """ check class Base documentation """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_functions(self):
        """ check documentation for every function """
        for item in self.list_base_functions:
            function = item[1]
            self.assertTrue(len(function.__doc__) >= 1)


class TestBase(unittest.TestCase):
    """ Test Base """

    def setUp(self):
        """ Method called to prepare the test fixture """
        Base._Base__nb_objects = 0

    def test_not_arguments(self):
        """ test not args"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id(self):
        """ test id"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_arguments(self):
        """ test base args"""
        b1 = Base(10)
        b2 = Base(98)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 98)

    def test_many_arguments(self):
        """ test many args """
        with self.assertRaises(TypeError):
            b1 = Base(1, 5, 50)

    def test_private_attribute(self):
        """ test private attr"""
        b1 = Base()
        b1 = Base(100)
        with self.assertRaises(AttributeError):
            print(b1.__nb_objects)

        with self.assertRaises(AttributeError):
            print(b1.nb_objects)


if __name__ == "__main__":
    unittest.main()
