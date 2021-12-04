import unittest
import sys

def f(filename):
    h = 0
    v = 0
    with open(filename) as f:
        lines = [x.replace("\n", "").split(" ") for x in f.readlines()]
        for command in lines:
            c, p = (command[0], int(command[1]))
            if "forward" == c:
                h += p
            elif "up" == c:
                v -= p
            elif "down" == c:
                v += p
            else:
                print("unknown: " + c)
                sys.exit(1)
    return (h, v)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/02-part1.txt'), (15, 10))
        self.assertEqual(f('data/02-input.txt'), (1988, 913))

if __name__ == "__main__":
    unittest.main()
