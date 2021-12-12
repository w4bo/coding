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
                for neigh in graph[cur_node]:
                    if not neigh.islower() or neigh.islower() and neigh not in visited:
                        n_acc = [x for x in acc] 
                        n_acc.append(neigh)
                        n_visited = [x for x in visited]
                        n_visited.append(neigh)
                        rec(neigh, n_visited, n_acc)
        
        rec("start", ["start"], ["start"])
        return len(accs)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/12-test.txt'), 10)
        self.assertEqual(f('data/12-input.txt'), 3450)

if __name__ == "__main__":
    unittest.main()
