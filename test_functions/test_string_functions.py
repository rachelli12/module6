import unittest
import unittest.mock as mock
from more_functions import string_functions as sf

class MyTestCAse(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual('hellohellohello', sf.multiply_string('hello', 3))

if __name__ == '__main__':
    unittest.main()
