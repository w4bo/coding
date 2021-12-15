import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [[int(y) for y in x.strip()] for x in f.readlines()]  # read the lines
        # set the costs
        costs = {}
        unvisited = {}
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                costs[(i, j)] = c
                unvisited[(i, j)] = float("+inf")

        unvisited[(0, 0)] = 0
        visited = {}

        def dijkstra():
            def check_neighbors(x, y):
                cost = unvisited[(x, y)]
                if x + 1 < len(lines) and (x + 1, y) in unvisited:
                    unvisited[(x + 1, y)] = min(unvisited.get((x + 1, y), float("+inf")), cost + costs[(x + 1, y)])
                if y + 1 < len(lines[0]) and (x, y + 1) in unvisited:
                    unvisited[(x, y + 1)] = min(unvisited.get((x, y + 1), float("+inf")), cost  + costs[(x, y  + 1)])
                visited[(x, y)] = cost
                unvisited.pop((x, y))
            
            while len(unvisited) > 0:
                x, y = min(unvisited, key=unvisited.get)
                check_neighbors(x, y)
        
        dijkstra()
        return visited[(len(lines) - 1, len(lines[0]) - 1)]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/15-test.txt'), 40)
        self.assertEqual(f('data/15-input.txt'), 745)

if __name__ == "__main__":
    unittest.main()
