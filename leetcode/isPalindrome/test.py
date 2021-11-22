import unittest
from importlib import import_module
import sys
sys.path.insert(0, 'isPalindrome')
from v1 import test_function


def unit_test(self, test_function):
    self.assertTrue(test_function(121))
    self.assertTrue(test_function(11))
    self.assertTrue(test_function(0))
    self.assertFalse(test_function(-121))
    self.assertFalse(test_function(123))
    self.assertFalse(test_function(12))

class MyTest(unittest.TestCase):
    def test(self):
        unit_test(self, test_function)

if __name__ == "__main__":
    unittest.main()