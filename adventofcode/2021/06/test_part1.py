import unittest
import sys

def f(filename, days):
    with open(filename) as f:
        curstatus = [int(x) for x in f.readlines()[0].split(",")]  # read the lines
        for d in range(days):
            newfishes = []
            for i, c in enumerate(curstatus):
                if c == 0:
                    curstatus[i] = 6
                    newfishes.append(8)
                else:
                    curstatus[i] -= 1
            curstatus.extend(newfishes)
    return len(curstatus)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/06-test.txt', 18), 26)
        self.assertEqual(f('data/06-test.txt', 80), 5934)
        self.assertEqual(f('data/06-input.txt', 80), 362666)

if __name__ == "__main__":
    unittest.main()
