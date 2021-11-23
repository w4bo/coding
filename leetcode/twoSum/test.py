import unittest
import os
from importlib import import_module
import time
import sys
sys.path.insert(0, 'twoSum')
from v2 import test_function

def unit_test(self, twoSum):
    self.assertEqual(set(twoSum([2, 7, 11, 15], 9)), set([0, 1]))
    self.assertEqual(set(twoSum([3, 2, 4], 6)), set([1, 2]))
    self.assertEqual(set(twoSum([3, 3], 6)), set([0, 1]))
    self.assertEqual(set(twoSum([-3, 4, 3, 90], 0)), set([0, 2]))

class TwoSum(unittest.TestCase):
    def test(self):
        unit_test(self, test_function)

if __name__ == "__main__":
    unittest.main()