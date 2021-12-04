import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [x.replace("\n", "") for x in f.readlines()]  # read the lines
        numbers = [int(x) for x in lines[0].split(",")]
        
        boards = []
        lines = lines[2:]
        i = 0
        skip_line = False
        while i < len(lines):
            if not skip_line:
                boards.append([[int(y) for y in x.split(' ') if len(y) > 0] for x in lines[i: i+5]])
                i += 5
                skip_line = True
            else:
                i += 1
                skip_line = False

        for n in numbers:
            for board in boards:
                for line in board:  # iterate over the line
                    for i, c in enumerate(line):  # if the line contains the number...
                        if c == n:
                            line[i] = -1
                for i in range(5):
                    winning_r = sum(board[i]) == -5  # a board is winning if the line is full of -1s
                    winning_c = 0
                    for j in range(5): # or if a column is full of -1s
                        winning_c += board[j][i]
                    winning_c = winning_c == -5
                    if winning_r or winning_c:
                        return sum([sum([x for x in line if x > 0]) for line in board]) * n
    return -1


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/04-test.txt'), 4512)
        self.assertEqual(f('data/04-input.txt'), 2745)

if __name__ == "__main__":
    unittest.main()
