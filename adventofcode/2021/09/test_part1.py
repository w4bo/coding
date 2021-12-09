import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [[int(y) for y in x.strip()] for x in f.readlines()]  # read the lines
        mins = []
        for i, r in enumerate(lines):  # rows
            for j, c in enumerate(lines[i]):  # cols
                left, right, up, down = float('inf'), float('inf'), float('inf'), float('inf')
                if j - 1 >= 0:
                    left = lines[i][j - 1]
                if j + 1 < len(lines[i]):
                    right = lines[i][j + 1]
                if i - 1 >= 0:
                    up = lines[i - 1][j]
                if i + 1 < len(lines):
                    down = lines[i + 1][j]
                if c < left and c < right and c < up and c < down:
                    mins.append(c + 1) 
        return sum(mins)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/09-test.txt'), 15)
        self.assertEqual(f('data/09-input.txt'), 526)

if __name__ == "__main__":
    unittest.main()
