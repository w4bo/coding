import unittest
from importlib import import_module
import sys
sys.path.insert(0, 'longestPalindrome')
from v1 import test_function


def unit_test(self, test_function):
    self.assertEqual(test_function("daaaaaaa"), "aaaaaaa")
    self.assertEqual(test_function("dadbbbbada"), "bbbb")
    self.assertEqual(test_function("babad"), "bab")
    self.assertEqual(test_function("anna"), "anna")
    self.assertEqual(test_function("cbbd"), "bb")
    self.assertEqual(test_function("a"), "a")
    self.assertEqual(test_function("bcdcb"), "bcdcb")
    self.assertEqual(test_function("adaa"), "ada")
    self.assertEqual(test_function("aaada"), "aaa")
    self.assertEqual(test_function("asdasdasdbb"), "bb")
    self.assertEqual(test_function("bb"), "bb")
    self.assertEqual(test_function("bbb"), "bbb")


class MyTest(unittest.TestCase):
    def test(self):
        unit_test(self, test_function)


if __name__ == "__main__":
    unittest.main()
