import unittest
import os
from importlib import import_module
import time

def unit_test(self, twoSum):
    self.assertEqual(set(twoSum([2, 7, 11, 15], 9)), set([0, 1]))
    self.assertEqual(set(twoSum([3, 2, 4], 6)), set([1, 2]))
    self.assertEqual(set(twoSum([3, 3], 6)), set([0, 1]))
    self.assertEqual(set(twoSum([-3, 4, 3, 90], 0)), set([0, 2]))

class TwoSum(unittest.TestCase):
    def test(self):
        res = {}
        for filename in os.listdir("."):
            if filename.endswith(".py") and filename != "test.py": 
                module = import_module(filename.replace(".py", ""))
                test_function = module.test_function
                trials = 10
                start = time.time()
                for i in range(trials):
                    unit_test(self, test_function)
                res[filename] = (time.time() - start) / trials
        print({k: v for k, v in sorted(res.items(), key=lambda item: item[1])})

if __name__ == "__main__":
    unittest.main()