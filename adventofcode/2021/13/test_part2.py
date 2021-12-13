import unittest
import sys

def print_board(dots):
    max_x = 0
    max_y = 0
    for k, v in dots.items():
        x, y = k
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    s = ""
    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            v = dots.get((x, y), 0)
            s += "#" if v > 0 else "."
        s += "\n"
    print(s)
    with open("out.txt", "w") as f:
        f.write(s)

def f(filename):
    with open(filename) as f:
        lines = [x.strip() for x in f.readlines()]  # read the lines

        dots = {}
        instructions = []

        
        f = False
        for line in lines:
            f = f or len(line) == 0
            if f:
                if len(line) > 0:
                    line = line.split("=")
                    instructions.append((line[0][-1], int(line[1])))
            else:
                line = [x for x in line.split(",")]
                y = int(line[0])
                x = int(line[1])
                dots[(x, y)] = 1

        for f, idx in instructions:
            to_remove = []
            new_dots = {}
            for coord, v in dots.items():
                x, y = coord
                if f == "y" and x > idx or f == "x" and y > idx:
                    to_remove.append(coord)
                    new_dots[((idx + idx - x) if f == "y" else x, (idx + idx - y) if f == "x" else y)] = 1
            
            dots = {**dots, **new_dots}
            for r in to_remove:
                del dots[r]

        print_board(dots)     
        return len(dots)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/13-input.txt'), 97)

if __name__ == "__main__":
    unittest.main()
