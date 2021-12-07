import unittest
import sys

def cost(try_pos, curpositions):
    cost = 0
    for cur_pos in curpositions:
        diff = sum(range(1, abs(cur_pos - try_pos) + 1))
        cost += diff
    return cost
    
def f(filename):
    with open(filename) as f:
        cur_positions = sorted([int(x) for x in f.readlines()[0].split(",")])  # read the lines
        opt_pos = cur_positions[0]
        opt_cost = cost(cur_positions[0], cur_positions)
        for c in range(cur_positions[0], cur_positions[-1] + 1):
            cur_cost = cost(c, cur_positions)
            if cur_cost <= opt_cost:
                opt_cost = cur_cost
                opt_pos = c
            else:
                return opt_cost
        return opt_cost


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/07-test.txt'), 168)
        self.assertEqual(f('data/07-input.txt'), 93397632)

if __name__ == "__main__":
    unittest.main()
