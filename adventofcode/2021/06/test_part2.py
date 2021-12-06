import unittest
import sys

def f(filename, days):
    with open(filename) as f:
        curstatus = [int(x) for x in f.readlines()[0].split(",")]  # read the lines
        smart_status = {}
        for c in curstatus:
            if c not in smart_status:
                smart_status[c] = 0
            smart_status[c] += 1
        curstatus = smart_status
        for d in range(days):
            print("Day " + str(d))
            newstatus = {}
            for k, v in curstatus.items():
                if k == 0:
                    newstatus[8] = v
                    newstatus[6] = v + newstatus.get(6, 0)
                else:
                    newstatus[k - 1] = v + newstatus.get(k - 1, 0)
            curstatus = newstatus
        c = 0
        for k, v in curstatus.items():
            c += v
    return c


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/06-testa.txt', 9), 2)
        self.assertEqual(f('data/06-testa.txt', 16), 3)
        self.assertEqual(f('data/06-test.txt', 18), 26)
        self.assertEqual(f('data/06-test.txt', 80), 5934)
        self.assertEqual(f('data/06-test.txt', 256), 26984457539)
        self.assertEqual(f('data/06-input.txt', 80), 362666)
        self.assertEqual(f('data/06-input.txt', 256), 26984457539)

if __name__ == "__main__":
    unittest.main()
