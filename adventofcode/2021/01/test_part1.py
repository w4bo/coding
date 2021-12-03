import unittest

def f():
    with open('data/01-input.txt') as f:
        lines = [int(x.replace("\n", "")) for x in f.readlines()]
        c = 0
        prev = lines[0]
        for cur in lines[1:]:
            if cur > prev:
                c += 1
            prev = cur
    return c


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f(), 1752)

if __name__ == "__main__":
    unittest.main()
