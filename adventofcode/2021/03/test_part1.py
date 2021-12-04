import unittest
import sys

def f(filename):
    with open(filename) as f:
        lines = [x.replace("\n", "") for x in f.readlines()]  # read the lines
        counts = [int(x) for x in lines[0]]  # count the 1s
        count = len(lines)  # get the number of lines
        for line in lines[1:]:  # iterate over the lines...
            for i in range(len(line)):  # iterate over each line...
                if line[i] == "1":  # if the current element is 1
                    counts[i] += 1  # increment the counter
        gamma = 0
        epsilon = 0
        k = len(counts) - 1
        for i in range(len(counts)):  # iterate over the 1s counter
            most = 0  # most frequent bit
            least = 1  # least frequent bit
            if counts[i] > int(count / 2):  # if the 1s are the majority...
                most = 1
                least = 0
            gamma += most * pow(2, k - i) # 1s are stored in reverse order, so I need k - i
            epsilon += least * pow(2, k - i)
    return (gamma, epsilon)


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/03-test.txt'), (22, 9))
        self.assertEqual(f('data/03-input.txt'), (1143, 2952))

if __name__ == "__main__":
    unittest.main()
