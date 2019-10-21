#!/usr/bin/python3
""" Test for class Base """
import unittest
import inspect
from models import base
Base = base.Base


class TestBaseDocumentation(unittest.TestCase):
    """ calss to check documentation for Base class """

    @classmethod
    def setUpClass(cls):
        """ This method run before all test and
            find into Base class all functions. it store in a list of tuples """
        cls.list_base_functions = inspect.getmembers(Base, inspect.isfunction)

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
    def test_not_arguments(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_not_arguments_other_instance(self):
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_arguments(self):
        b1 = Base(10)
        b2 = Base(98)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 98)

    def test_many_arguments(self):
        with self.assertRaises(TypeError):
            b1 = Base(1, 5, 50)

    def test_private_attribute(self):
        b1 = Base()
        b1 = Base(100)
        with self.assertRaises(AttributeError):
            b1.__nb_objects

        with self.assertRaises(AttributeError):
            b1.nb_objects


if __name__ == "__main__":
    unittest.main()
