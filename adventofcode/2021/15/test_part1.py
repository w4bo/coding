import heapq
import unittest


def f(filename):
    with open(filename) as f:
        lines = [[int(y) for y in x.strip()] for x in f.readlines()]  # read the lines

        costs = {}
        unvisited = []
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if i != 0 or j != 0:
                    costs[(i, j)] = float("+inf")
                else:
                    costs[(0, 0)] = 0
                    heapq.heappush(unvisited, (0, 0, 0))
        visited = set()
        max_x = len(lines)
        max_y = len(lines[0])

        def dijkstra():
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
                cost, x, y = heapq.heappop(unvisited)
                if (x, y) not in visited:
                    visited.add((x, y))
                    check_neighbors(cost, x, y)
                    if x == max_x - 1 and y == max_y - 1:
                        break

        dijkstra()
        return costs[(len(lines) - 1, len(lines[0]) - 1)]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/15-test.txt'), 40)
        self.assertEqual(f('data/15-input.txt'), 745)


if __name__ == "__main__":
    unittest.main()
