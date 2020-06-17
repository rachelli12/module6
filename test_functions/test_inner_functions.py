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
        self.assertEqual(ifa.measurements([5.6, 8.9]), "Perimeter=22.4 Area=31.4")

    def test_measurements_square(self):
        self.assertEqual(ifa.measurements([4.2]), "Perimeter=16.8 Area=17.6")

if __name__ =="__main__":
    unittest.main()
