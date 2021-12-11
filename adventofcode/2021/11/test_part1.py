import unittest
import sys

def f(filename, d):
    with open(filename) as f:
        octopuses = [[int(y) for y in x.strip()] for x in f.readlines()]  # read the lines
        
        flashes = 0
        for d in range(d):
            to_flash = set()

            def inc(i, j):
                if i >= 0 and i < len(octopuses) and j >= 0 and j < len(octopuses[i]) and octopuses[i][j] <= 9:
                    octopuses[i][j] += 1
                    if octopuses[i][j] > 9:
                        to_flash.add((i, j))

            # increase each octopus
            for i, line in enumerate(octopuses):
                for j, y in enumerate(line):
                    inc(i, j)

            flashed = set()
            while len(to_flash) > 0:
                (i, j) = to_flash.pop()
                flashed.add((i, j))
                flashes += 1
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        inc(i + a, j + b)
            
            while len(flashed) > 0:
                (i, j) = flashed.pop()
                octopuses[i][j] = 0

        return flashes


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/11-testa.txt', 2), 9)
        self.assertEqual(f('data/11-test.txt', 100), 1656)
        self.assertEqual(f('data/11-input.txt', 100), 1655)

if __name__ == "__main__":
    unittest.main()
