import unittest
import math
from functools import reduce


def hex_to_bin(hex):
    if hex == "F":
        return "1111"
    elif hex == "E":
        return "1110"
    elif hex == "D":
        return "1101"
    elif hex == "C":
        return "1100"
    elif hex == "B":
        return "1011"
    elif hex == "A":
        return "1010"
    elif hex == "9":
        return "1001"
    elif hex == "8":
        return "1000"
    elif hex == "7":
        return "0111"
    elif hex == "6":
        return "0110"
    elif hex == "5":
        return "0101"
    elif hex == "4":
        return "0100"
    elif hex == "3":
        return "0011"
    elif hex == "2":
        return "0010"
    elif hex == "1":
        return "0001"
    elif hex == "0":
        return "0000"


def bin_to_num(bin):
    c = 0
    for i, x in enumerate(bin):
        c += int(x) * pow(2, len(bin) - 1 - i)
    return c


def reduces(nums, typeId):
    if typeId == 0:
        return sum(nums)
    elif typeId == 1:
        return reduce((lambda x, y: x * y), nums)
    elif typeId == 2:
        return min(nums)
    elif typeId == 3:
        return max(nums)
    elif typeId == 5:
        return 1 if nums[0] > nums[1] else 0
    elif typeId == 6:
        return 1 if nums[0] < nums[1] else 0
    elif typeId == 7:
        return 1 if nums[0] == nums[1] else 0


def from_file(filename):
    with open(filename) as file:
        lines = [x.strip() for x in file.readlines()][0]  # read the lines
        return f(lines)


def f(lines):
    lines = ''.join([hex_to_bin(y) for y in lines])  # read the lines

    def parse(lines):
        V = bin_to_num(lines[0:3])
        T = bin_to_num(lines[3:6])
        if T == 4:
            s = ""
            lines = lines[6:]
            flag = True
            while flag:
                if lines[0] == "0":
                    flag = False
                cur = lines[1:5]
                if len(cur) == 4:
                    s += cur
                lines = lines[5:]
            return (lines, bin_to_num(s))
        else:
            I = lines[6]
            nums = []
            if I == "0":
                subpacket_length = bin_to_num(lines[7:22])
                lines = lines[22:]
                i = 0
                while i < subpacket_length:
                    prev = len(lines)
                    lines, num = parse(lines)
                    nums.append(num)
                    i += prev - len(lines)
            else:
                subpackets = bin_to_num(lines[7:18])
                lines = lines[18:]
                for i in range(subpackets):
                    lines, num = parse(lines)
                    nums.append(num)
            return lines, reduces(nums, T)

    lines, v = parse(lines)
    return v


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('C200B40A82'), 3)
        self.assertEqual(f('04005AC33890'), 54)
        self.assertEqual(from_file('data/16-input.txt'), 6802496672062)


if __name__ == "__main__":
    unittest.main()
