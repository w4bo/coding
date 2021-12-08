import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [[y.split(" ") for y in x.strip().split(" | ")] for x in f.readlines()]  # read the lines
        outputs = [x[1] for x in lines]
        digits = {}
        for output in outputs:
            for o in output:
                digits[len(o)] = 1 + digits.get(len(o), 0)
        return digits[2] + digits[3] + digits[4] + digits[7]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/08-test.txt'), 26)
        self.assertEqual(f('data/08-input.txt'), 288)

if __name__ == "__main__":
    unittest.main()
