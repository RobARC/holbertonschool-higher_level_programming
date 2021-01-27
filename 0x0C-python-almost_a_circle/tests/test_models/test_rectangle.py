#!/usr/bin/python3
"""Test Rectangle"""
import unittest
from models.base import Base
from models.square import Square
import os
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO
import fileinput

class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class instantiation tests"""

    def test1main(self):
        """tests file main 1"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_readme(self):
        """tests README file"""
        readme = os.getcwd()
        readme1 = readme +'/README.md'
        readme2 = os.path.exists(readme1)
        self.assertEqual(readme2, True)

    def test_pep8(self):
        case = '\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with os.popen("pep8 models/base.py") as cmd:
                print(cmd.read())
            self.assertEqual(fake_out.getvalue(), case)

    def test_sheban(self):
        """tests sheban """
        path1 = os.getcwd()
        filename1 = path1 +'/models/base.py'
        expected = ''
        print(filename1)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            send_cmd = os.system('pep8 filename1')
            self.assertEqual(fake_out.getvalue(), expected)

    def test_cases_main2(self):
        """tests file main 2"""

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
        """tests file main 3"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_cases_main4(self):
        """tests file main 4"""
        output1 = "####\n####\n####\n####\n####\n####\n"
        r1 = Rectangle(4, 6)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), output1)  

        output2 = "##\n##\n"
        r1 = Rectangle(2, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
           r1.display()
           self.assertEqual(fake_out.getvalue(), output2)

    def test_cases_main5(self):
        """tests file main 5"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6" 
        self.assertEqual(str(r1), expected)
        
        output =  "[Rectangle] (12) 2/1 - 4/6\n"
        with patch("sys.stdout", new = StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), output)

        r2 = Rectangle(5, 5, 1)
        expected = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(str(r2), expected)
        
        output1 = "[Rectangle] (1) 1/0 - 5/5\n"
        with patch("sys.stdout", new = StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), output1)

    def test_cases_main6(self):
        """tests file main 6"""
        output0 = "\n\n  ##\n  ##\n  ##\n"
        r1 = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), output0)

        output0 = " ###\n ###\n"
        r1 = Rectangle(3, 2, 1, 0)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), output0)

    def test_cases_main7(self):
        """tests file main 7"""
        r1 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (1) 10/10 - 10/10" 
        self.assertEqual(str(r1), expected)

        r1.update(89)
        expected = "[Rectangle] (89) 10/10 - 10/10" 
        self.assertEqual(str(r1), expected)
        
        r1.update(89, 2)
        expected = "[Rectangle] (89) 10/10 - 2/10" 
        self.assertEqual(str(r1), expected)

        r1.update(89, 2, 3)
        expected = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(str(r1), expected)

        r1.update(89, 2, 3, 4)
        expected = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(str(r1), expected)

        r1.update(89, 2, 3, 4, 5)
        expected = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(str(r1), expected)

    def test_cases_main8(self):
        """tests file main 8"""
        r1 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (1) 10/10 - 10/10" 
        self.assertEqual(str(r1), expected)
        
        r1.update(height=1)
        expected = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(str(r1), expected)

        r1.update(width=1, x=2)
        expected = "[Rectangle] (1) 2/10 - 1/1"
        self.assertEqual(str(r1), expected)

        r1.update(y=1, width=2, x=3, id=89)
        expected = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(r1), expected)

        r1.update(x=1, height=2, y=3, width=4)
        expected = "[Rectangle] (89) 1/3 - 4/2" 
        self.assertEqual(str(r1), expected)

    def test_cases_main9(self):
        """tests file main 9"""
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

    
    def test_instance_class(self):
        """Checks for a instance of the class
        """
        r1 = Rectangle(10, 2)
        self.assertIsInstance(r1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        r2 = Rectangle(2, 5)
        self.assertTrue(type(r1) == type(r2))
        self.assertFalse(id(r1) == id(r2))
            
    def tearDown(self):
        Base._Base__nb_objects = 0

if __name__ == '__main__':
    unittest.main()
