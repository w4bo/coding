import unittest
import sys

def f(filename, d):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]  # read the lines
        template = lines[0]
        instructions = [x.split(" -> ") for x in lines[2:]]
        instructions = {x[0]: x[1] for x in instructions}
        
        for d in range(d):
            i = 0
            while i < len(template) - 1:
                pair = template[i] + template[i + 1]
                if pair in instructions:
                    template = template[:i + 1] + instructions[pair] + template[i+1:]
                    i += 2
                else:
                    i += 1

        res = {}
        for c in template:
            res[c] = res.get(c, 0) + 1 

        acc = []
        for k, v in res.items():
            acc.append(v)
        
        acc = sorted(acc)
        return acc[-1] - acc[0]

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/14-test.txt', 10), 1588)
        self.assertEqual(f('data/14-input.txt', 10), 3230)

if __name__ == "__main__":
    unittest.main()
