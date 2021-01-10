#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestFunctionMaxInteger(unittest.TestCase):
    """
    Define a Class to test all diferent cases in
    6-max_integer.py
    """
    def test_integer_num(self):
        """ Checks for integer numbers"""
        # Positive Numbers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Negative Numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Negative and Positive
        self.assertEqual(max_integer([1, -2, -3, 4]), 4)

        # One integer
        self.assertEqual(max_integer([3]), 3)

        # One negative integer
        self.assertEqual(max_integer([-3]), -3)

        # Max at the begin
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

        # Max in the middle
        self.assertEqual(max_integer([1, 2, 3, 4, 3, 2, 1]), 4)

        # List Empty
        self.assertEqual(max_integer([]), None)

    def test_float_num(self):
        # Positive Float Numbers
        self.assertEqual(max_integer([1.8, 2.24, 3.35, 4.4]), 4.4)
        # Negative Float Numbers
        self.assertEqual(max_integer([-1.8, -2.24, -3.35, -4.4]),     -1.8)

    def test_strings(self):
        """Checks for strings like arguments"""
        self.assertEqual(max_integer(['Roberth']), 'Roberth')
