import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]  # read the lines
        acc = 0
        for line in lines:
            stack = []
            for c in line:
                if c == "(" or c == "[" or c == "{" or c == "<":
                    stack.append(c)
                else:
                    p = stack.pop()
                    if c == ")" and p != "(":
                        acc += 3
                    elif c == "]" and p != "[":
                        acc += 57
                    elif c == "}" and p != "{":
                        acc += 1197
                    elif c == ">" and p != "<":
                        acc += 25137
        return acc


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/10-test.txt'), 26397)
        self.assertEqual(f('data/10-input.txt'), 311895)

if __name__ == "__main__":
    unittest.main()
