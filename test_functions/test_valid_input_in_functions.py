"""
Program name: test_valid_input_in_functions.py
Author: Rachel Li
Last date modified: 06/16/2020

The purpose of this program is to
"""
import unittest
import unittest.mock as mock
from more_functions import validate_input_in_functions as vif

class MyTestCase(unittest.TestCase):
    test_name = 'English'
    def test_score_input_test_name(self):
        test_score = None
        self.assertEqual("English", vif.score_input("English", test_score, invalid_message=None))
    def test_score_input_test_score_below_range(self):
        test_score = -45
        self.assertEqual("English: -45", vif.score_input("English", test_score, invalid_message="Please try again"))
    def test_score_input_test_score_above_range(self):
        test_score = 120
        self.assertEqual("English: 120", vif.score_input("English", test_score, invalid_message="Please try again"))
    def test_test_score_non_numeric(self):
        test_score = 'Fail'
        self.assertEqual("English: Fail", vif.score_input("English", test_score, invalid_message="Please try again"))
    def test_score_input_invalid_message(self):
        test_score = 89
        self.assertEqual("English: 89", vif.score_input("English", test_score, invalid_message="Please try again"))

if __name__ == '__main__':
    unittest.main()
