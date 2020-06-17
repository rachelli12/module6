"""
Program name: test_inner_functions,py
Author: Rachel Li
Last date modified: 16/06/2020

This program tests inner_functions_assignment.py
"""
import unittest
import unittest.mock as mock
from source_files import inner_functions_assignment as ifa

class MyTestCase(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(ifa.measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertRaises(ifa.measurements([3.5]), "Perimeter = 14.0 Area = 12.25")

if __name__ =="__main__":
    unittest.main()
