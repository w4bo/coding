import unittest
import sys

def f(filename):

    def inc(a, b, c):
        if a < b:
            c += 1
        elif a == b:
            c += 0
        else:
            c += -1
        return c

    with open(filename) as f:
        lines = [[int(y) for y in x.replace("\n", "").replace(" -> ", ",").split(",")] for x in f.readlines()]  # read the lines
        coverage = {}
        for line in lines:
            x_s = line[0]
            y_s = line[1]
            x_e = line[2]
            y_e = line[3]

            if y_s == y_e and x_s != x_e or x_s == x_e and y_s != y_e:
                x = x_s
                y = y_s
                while x != x_e or y != y_e:
                    if (x, y) not in coverage:
                        coverage[(x, y)] = 0
                    coverage[(x, y)] += 1
                    y = inc(y_s, y_e, y)
                    x = inc(x_s, x_e, x)
                if (x, y) not in coverage:
                    coverage[(x, y)] = 0
                coverage[(x, y)] += 1

    return len([key for key, value in coverage.items() if value > 1])


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/05-testa.txt'), 0)
        self.assertEqual(f('data/05-test.txt'), 5)
        self.assertEqual(f('data/05-input.txt'), 5280)

if __name__ == "__main__":
    unittest.main()
