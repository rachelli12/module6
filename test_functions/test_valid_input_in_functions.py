"""
Program name: test_valid_input_in_functions.py
Author: Rachel Li
Last date modified: 06/16/2020

The purpose of this program is to test validate_input_in_functions.py
"""
import unittest
import unittest.mock as mock
from more_functions import validate_input_in_functions as vif

class MyTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        #only mandatory argument
        self.assertEqual(vif.score_input("English"), "English: 0")
    def test_score_input_test_score_valid(self):
        #one good input
        test_score = 89
        self.assertEqual(vif.score_input("English", test_score),"English: 89")
    def test_score_input_test_score_below_range(self):
        #one below range
        test_score = -45
        self.assertEqual(vif.score_input("English", test_score), "Please try again")
    def test_score_input_test_score_above_range(self):
        #one above range
        test_score = 120
        self.assertEqual(vif.score_input("English", test_score), "Please try again")
    def test_test_score_non_numeric(self):
        #one non-numeric input, must account for exception
        with self.assertRaises(ValueError):
            test_score = 'fail'
            vif.score_input("English", test_score)
    def test_score_input_invalid_message(self):
        #has all arguments
        test_score = 102
        self.assertEqual(vif.score_input("English", test_score, invalid_message="Please try again"), "Please try again")


if __name__ == '__main__':
    unittest.main()
