#!/usr/bin/python3
"""Test Square"""
import unittest
from models.base import Base
from models.square import Square
import os
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO

class TestSquare(unittest.TestCase):
    """Test class for Square class instantiation tests"""

    def test_readme(self):
        """tests README file"""
        readme = os.getcwd()
        readme1 = readme +'/README.md'
        readme2 = os.path.exists(readme1)
        self.assertEqual(readme2, True)

    def test_cases_main9(self):
        s1 = Square(5)
        expected = "[Square] (1) 0/0 - 5\n"
        expected1 = '25\n'
        expected2 = "#####\n#####\n#####\n#####\n#####\n"

        with patch("sys.stdout", new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), expected)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1.area())
            self.assertEqual(fake_out.getvalue(), expected1)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), expected2)

        s2 = Square(2, 2)
        expected = "[Square] (1) 0/0 - 5\n"
        expected1 = '25\n'
        expected2 = "#####\n#####\n#####\n#####\n#####\n"

        with patch("sys.stdout", new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), expected)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            print(s1.area())
            self.assertEqual(fake_out.getvalue(), expected1)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            s1.display()
            self.assertEqual(fake_out.getvalue(), expected2)

    def test_cases_main10(self):
    
        s1 = Square(5)
        
        expected = "[Square] (1) 0/0 - 5\n"
        expected1 = '5\n'
        expected2 = "[Square] (1) 0/0 - 10\n"
        expected3 = "[TypeError] width must be an integer"
        
        with patch("sys.stdout", new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), expected)
        
        with patch("sys.stdout", new = StringIO()) as fake_out:
            print(s1.size)
            self.assertEqual(fake_out.getvalue(), expected1)
        
        
        s1.size = 10
        self.assertEqual(s1.size, 10)


        with patch("sys.stdout", new = StringIO()) as fake_out:
            print(s1)
            self.assertEqual(fake_out.getvalue(), expected2)

        with self.assertRaises(TypeError):
            s1.size = "9" 

    def test_getter(self):
        r1 = Square(5)
        self.assertEqual(r1.size, 5)

    def test_setter(self):
        r1 = Square(5)
        r1.size = 8
        self.assertEqual(r1.size, 8)

    def test_string(self):
        r1 = Square(3)
        with self.assertRaises(TypeError):
            r1.size = "Hello"
    def test_negative(self):
        r1 = Square(6)
        with self.assertRaises(ValueError):
            r1.size = -5
    def test_numreal(self):
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = 1.5
    def test_tuplas(self):
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = (2, 8)
    def test_empty(self):
        r1 = Square(7)
        with self.assertRaises(TypeError):
            r1.size = ""
    def test_none(self):
        r1 = Square(3)
        with self.assertRaises(TypeError):
            r1.size = None
    def test_list(self):
        r1 = Square(3)
        with self.assertRaises(TypeError):
            r1.size = [4, 7]
    def test_dict(self):
        r1 = Square(5)
        with self.assertRaises(TypeError):
            r1.size = {"hello": 5, "world": 8}
    def test_width(self):
        r1 = Square(5)
        r1.size =6
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)
    def test_to_dictionary(self):
        Base.__Base__nb_objects = 0
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 2, 'size': 10, 'y': 1} 
        self.assertEqual(s1_dictionary, expected)
        s1.update(5, 5, 5, 5)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 5, 'x': 5, 'size': 5, 'y': 5}
        self.assertEqual(s1_dictionary, expected)
        s1 = Square(1, 0, 0, 9)
        s1_dictionary = s1.to_dictionary()
        expected = {'id': 9, 'x': 0, 'size': 1, 'y': 0}
        self.assertEqual(s1_dictionary, expected)


    def tearDown(self):
        Base._Base__nb_objects = 0
    
if __name__ == '__main__':
    unittest.main()
