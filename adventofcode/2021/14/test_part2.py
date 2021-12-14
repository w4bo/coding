import unittest
import sys

def get_patterns(template):
    patterns = {}
    i = 0
    while i < len(template) - 1:
        pair = template[i] + template[i + 1]
        # patterns[pair] = patterns.get(pair, []) + [i]
        patterns[pair] = patterns.get(pair, 0) + 1
        i += 1
    return patterns

def f(filename, d):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]  # read the lines
        template = lines[0]
        instructions = [x.split(" -> ") for x in lines[2:]]
        instructions = {x[0]: x[1] for x in instructions}
        
        cur_patterns = get_patterns(template)
        for d in range(d):
            new_patterns = {}
            for k, v in cur_patterns.items():
                pair = k[0] + instructions[k]
                new_patterns[pair] = new_patterns.get(pair, 0) + v
                pair = instructions[k] + k[1]
                new_patterns[pair] = new_patterns.get(pair, 0) + v
            cur_patterns = new_patterns.copy()

        res = {template[-1]: 1}
        for k, v in cur_patterns.items():
            res[k[0]] = res.get(k[0], 0) + v

        acc = []
        for k, v in res.items():
            acc.append(v)
        
        acc = sorted(acc)
        return acc[-1] - acc[0]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/14-test.txt', 10), 1588)
        self.assertEqual(f('data/14-input.txt', 10), 3230)
        self.assertEqual(f('data/14-test.txt', 40), 2188189693529)
        self.assertEqual(f('data/14-input.txt', 40), 3542388214529)

if __name__ == "__main__":
    unittest.main()
