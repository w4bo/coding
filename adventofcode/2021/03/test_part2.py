import unittest
import sys

def f(filename, oxigen=True):
    with open(filename) as f:
        lines = [x.replace("\n", "") for x in f.readlines()]  # read the lines
        for i in range(len(lines[0])):  # iterate over the 1s counter
            count = len(lines)  # get the number of lines
            c = 0  # 1s counter
            for line in lines:  # iterate over the lines...
                if line[i] == "1":  # if the current element is 1
                    c += 1  # increment the counter
            # get the most frequent bit if oxigen is True, else get the least frequent bit
            c = 1 if not oxigen and c < count / 2 or oxigen and c >= count / 2 else 0
            lines = [line for line in lines if line[i] == str(c)]  # filter the lines
            if len(lines) == 1:
                break
        # get the decimal value
        x = lines[0]
        k = len(x) - 1
        c = 0
        for i in range(len(x)):  # iterate over the 1s counter
            c += int(x[i]) * pow(2, k - i) # 1s are stored in reverse order, so I need k - i
    return c


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual((f('data/03-test.txt', oxigen=True), f('data/03-test.txt', oxigen=False)), (23, 10))
        self.assertEqual((f('data/03-input.txt', oxigen=True) * f('data/03-input.txt', oxigen=False)), 4432698)

if __name__ == "__main__":
    unittest.main()
