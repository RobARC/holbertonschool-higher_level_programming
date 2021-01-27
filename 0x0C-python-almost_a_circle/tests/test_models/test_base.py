#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """
    Define a Class to test all diferent cases in
    base.py
    """
    def test_cases_main1(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_cases_main2(self):

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
    
    def test_cases_main3(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_id_positive(self):
        bo = Base(23)
        self.assertEqual(bo.id, 23)
        bo = Base(34)
        self.assertEqual(bo.id, 34)

    def test_id_negative(self):
        bo = Base(-4)
        self.assertEqual(bo.id, -4)
        bo = Base(-10)
        self.assertEqual(bo.id, -10)

    def test_id_none(self):
        bo = Base()
        self.assertEqual(bo.id, 1)
        bo = Base(None)
        self.assertEqual(bo.id, 2)

    def test_id_string(self):
        bo = Base("st")
        self.assertEqual(bo.id, "st")
        bo = Base("st2")
        self.assertEqual(bo.id, "st2")

    def test_type(self):
        """ Test type and instance """
        b = Base()
        self.assertEqual(type(b), Base)
        self.assertTrue(isinstance(b, Base))

    def test_to_json_string(self):
        """ Test to_json_string functionality """
        d = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        json_d = Base.to_json_string([d])
        self.assertTrue(isinstance(d, dict))
        self.assertTrue(isinstance(json_d, str))
        self.assertCountEqual(
        json_d, '{["id": 1, "x": 2, "y": 3, "width": 4, "height": 5]}')
        json_d_1 = Base.to_json_string(None)
        self.assertEqual(json_d_1, "[]")
        err = ("to_json_string() missing 1 required positional argument: " +
        "'list_dictionaries'")
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
            self.assertEqual(err, str(e.exception))
            err = "to_json_string() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            Base.to_json_string([{1, 2}], [{3, 4}])
            self.assertEqual(err, str(e.exception))


    def tearDown(self):
        Base._Base__nb_objects = 0

if __name__ == '__main__':
    unittest.main()


