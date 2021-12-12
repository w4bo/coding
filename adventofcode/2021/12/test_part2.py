import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [x.strip().split("-") for x in f.readlines()]  # read the lines

        graph = {}
        for line in lines:
            graph[line[0]] = graph.get(line[0], []) + [line[1]]
            graph[line[1]] = graph.get(line[1], []) + [line[0]]

        accs = []
        def rec(cur_node, visited, acc):
            if cur_node == "end":
                accs.append(acc)
            else:
                already_visited_single_small_cave_twice = len([k for k, v in visited.items() if v > 1 and k.islower()]) > 0
                c = 1 if already_visited_single_small_cave_twice else 2
                for neigh in graph[cur_node]:
                    if neigh != "start" and (not neigh.islower() or visited.get(neigh, 0) < c):
                        n_acc = acc.copy() + [neigh]
                        n_visited = visited.copy()
                        n_visited[neigh] = n_visited.get(neigh, 0) + 1
                        rec(neigh, n_visited, n_acc)
        
        rec("start", {"start": 1}, ["start"])
        return len(accs)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/12-test.txt'), 36)
        self.assertEqual(f('data/12-input.txt'), 96528)

if __name__ == "__main__":
    unittest.main()
