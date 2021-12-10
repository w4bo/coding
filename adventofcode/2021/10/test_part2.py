import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]  # read the lines
        scores = []
        for line in lines:
            stack = []
            broken = False
            for c in line:
                if c == "(" or c == "[" or c == "{" or c == "<":
                    stack.append(c)
                else:
                    p = stack.pop()
                    if c == ")" and p != "(" or c == "]" and p != "[" or c == "}" and p != "{" or c == ">" and p != "<":
                        broken = True
                        break
            score = 0
            while not broken and len(stack) > 0:
                score *= 5
                p = stack.pop()
                if p == "(":
                    score += 1
                elif p == "[":
                    score += 2
                elif p == "{":
                    score += 3
                if p == "<":
                    score += 4
            if score > 0:
                scores.append(score)
        return sorted(scores)[int(len(scores) / 2)]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/10-test.txt'), 288957)
        self.assertEqual(f('data/10-testb.txt'), 288957)
        self.assertEqual(f('data/10-testa.txt'), 294)
        self.assertEqual(f('data/10-input.txt'), 311895)

if __name__ == "__main__":
    unittest.main()
