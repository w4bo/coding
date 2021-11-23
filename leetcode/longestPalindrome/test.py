from v1 import test_function
import unittest
from importlib import import_module
import sys
sys.path.insert(0, 'longestPalindrome')
from v1 import test_function


def unit_test(self, test_function):
    self.assertEquals(test_function("daaaaaaa"), "aaaaaaa")
    self.assertEquals(test_function("dadbbbbada"), "bbbb")
    self.assertEquals(test_function("babad"), "bab")
    self.assertEquals(test_function("anna"), "anna")
    self.assertEquals(test_function("cbbd"), "bb")
    self.assertEquals(test_function("a"), "a")
    self.assertEquals(test_function("bcdcb"), "bcdcb")
    self.assertEquals(test_function("adaa"), "ada")
    self.assertEquals(test_function("aaada"), "aaa")
    self.assertEquals(test_function("asdasdasdbb"), "bb")
    self.assertEquals(test_function("bb"), "bb")
    self.assertEquals(test_function("bbb"), "bbb")


class MyTest(unittest.TestCase):
    def test(self):
        unit_test(self, test_function)


if __name__ == "__main__":
    unittest.main()
