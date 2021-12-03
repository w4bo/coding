import unittest

def f():
    with open('data/01-input.txt') as f:
        lines = [int(x.replace("\n", "")) for x in f.readlines()]
        c = 0
        prev = sum(lines[0: 3])
        for curi in range(3, len(lines)):
            l = lines[curi - 2: curi + 1]
            cur = sum(l)
            if cur > prev:
                c += 1
            prev = cur
    return c

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(), 1781)

if __name__ == "__main__":
    unittest.main()
