import unittest
import unittest.mock as mock
from more_functions import string_functions as sf

class MyTestCase(unittest.TestCase):
    def test_multiple_string_hello(self):
        message = "Hello"
        n = 3
        self.assertEqual("HelloHelloHello", sf.multiply_string(3, "Hello"))
    def test_multuple_string_cat(self):
        message = "cat"
        n = 6
        self.assertEqual("CatCatCatCatCatCat", sf.multiply_string(6, "Cat"))

if __name__ == '__main__':
    unittest.main()
