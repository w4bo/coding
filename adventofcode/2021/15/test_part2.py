import unittest
import sys
import time
import heapq

def f(filename):
    with open(filename) as f:
        lines = [[int(y) for y in x.strip()] for x in f.readlines()]  # read the lines
        
        new_lines = []
        for i in range(len(lines) * 5):
            line = []
            for j in range(len(lines[0]) * 5):
                n = (lines[i % len(lines)][j % len(lines[0])] + int(i / len(lines)) + int(j / len(lines[0])))
                line.append((n % 10) + (1 if n >= 10 else 0))
            new_lines.append(line)
        lines = new_lines

        # set the costs
        costs = {}
        unvisited = []
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if i != 0 or j != 0:
                    costs[(i, j)] = float("+inf")
                    # heapq.heappush(unvisited, (float("+inf"), i, j))
                else:
                    costs[(0, 0)] = 0
                    heapq.heappush(unvisited, (0, 0, 0))
        visited = set()
        max_x = len(lines)
        max_y = len(lines[0])
        def dijkstra():
            t1 = 0
            t2 = 0

            def check_neighbors(cost, x, y):
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if abs(i) + abs(j) == 1 and x + i >= 0 and x + i < len(lines) and y + j >= 0 and y + j < len(lines):
                            c1 = cost + lines[x + i][y + j]
                            c = costs[(x + i, y + j)]
                            if c1 < c:
                                costs[(x + i, y + j)] = c1
                                heapq.heappush(unvisited, (c1, x + i, y + j))
            
            while len(unvisited) > 0:
                start = time.time()
                cost, x, y = heapq.heappop(unvisited)
                t1 += time.time() - start
                if (x, y) not in visited:
                    visited.add((x, y))
                    start = time.time()
                    check_neighbors(cost, x, y)
                    if x == max_x - 1 and y == max_y - 1:
                        break
                    t2 += time.time() - start

        # print(t1)
        # print(t2)
        dijkstra()
        return costs[(max_x - 1, max_y - 1)]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/15-test.txt'), 315)
        self.assertEqual(f('data/15-input.txt'), 3002)

if __name__ == "__main__":
    unittest.main()
