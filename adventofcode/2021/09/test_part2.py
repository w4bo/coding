import unittest
import sys
import math 

def get(i, j, lines, default):
    left, right, up, down = default, default, default, default
    if j - 1 >= 0:
        left = lines[i][j - 1]
    if j + 1 < len(lines[i]):
        right = lines[i][j + 1]
    if i - 1 >= 0:
        up = lines[i - 1][j]
    if i + 1 < len(lines):
        down = lines[i + 1][j]
    return left, right, up, down

def f(filename):
    with open(filename) as f:
        lines = [[int(y) for y in x.strip()] for x in f.readlines()]  # read the lines
        labels = [[float('inf') if y != 9 else 9 for y in x] for x in lines]
        cur_label = 0
        
        # label the mins
        for i, r in enumerate(lines):  # rows
            for j, c in enumerate(lines[i]):  # cols
                left, right, up, down = get(i, j, lines, float('inf'))
                if c < left and c < right and c < up and c < down:
                    labels[i][j] = cur_label
                    cur_label += 1
                    if cur_label == 9:
                        cur_label += 1
        
        res = {}
        f = True  # exists at least a -1
        while f:
            f = False
            for i, r in enumerate(labels):  # rows
                for j, c in enumerate(labels[i]):  # cols
                    if c == float('inf'):
                        left, right, up, down = get(i, j, labels, 9)
                        l = [x for x in [c, left, right, up, down] if x != 9]
                        if len(l) > 0:
                            f = f or True
                            label = min(l)
                            if label != float('inf'):
                                labels[i][j] = label
                                res[label] = 1 + res.get(label, 1)

        acc = sorted([v for k, v in res.items()])[-3:]
        return math.prod(acc)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/09-test.txt'), 1134)
        self.assertEqual(f('data/09-input.txt'), 1123524)

if __name__ == "__main__":
    unittest.main()
