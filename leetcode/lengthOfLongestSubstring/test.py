import unittest
from importlib import import_module
import sys
sys.path.insert(0, 'lengthOfLongestSubstring')
from v1 import test_function

def unit_test(self, test_function):
    self.assertEquals(test_function("abc"), 3)
    self.assertEquals(test_function("ababc"), 3)
    self.assertEquals(test_function("abcabcbb"), 3)
    self.assertEquals(test_function("bbbbb"), 1)
    self.assertEquals(test_function("pwwkew"), 3)
    self.assertEquals(test_function("dvdf"), 3)

class MyTest(unittest.TestCase):
    def test(self):
        unit_test(self, test_function)

if __name__ == "__main__":
    unittest.main()