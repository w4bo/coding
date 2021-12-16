import unittest


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


res = {"acc": 0}


def f(filename):
    res["acc"] = 0
    with open(filename) as f:
        lines = [''.join([hex_to_bin(y) for y in x.strip()]) for x in f.readlines()][0]  # read the lines

        def parse(lines):
            V = bin_to_num(lines[0:3])
            res["acc"] += V
            T = bin_to_num(lines[3:6])
            s = ""
            if int(T) == 4:
                lines = lines[6:]
                flag = True
                while flag:
                    if lines[0] == "0":
                        flag = False
                    cur = lines[1:5]
                    if len(cur) == 4:
                        s += cur
                    lines = lines[5:]
                return lines
            else:
                I = lines[6]
                if I == "0":
                    subpacket_length = bin_to_num(lines[7:22])
                    lines = lines[22:]
                    i = 0
                    while i < subpacket_length:
                        prev = len(lines)
                        lines = parse(lines)
                        i += prev - len(lines)
                    return lines
                else:
                    subpackets = bin_to_num(lines[7:18])
                    lines = lines[18:]
                    for i in range(subpackets):
                        lines = parse(lines)
                    return lines

        parse(lines)
        return res["acc"]


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/16-test.txt'), 6)
        self.assertEqual(f('data/16-testb.txt'), 9)
        self.assertEqual(f('data/16-testc.txt'), 14)
        self.assertEqual(f('data/16-testd.txt'), 16)
        self.assertEqual(f('data/16-teste.txt'), 12)
        self.assertEqual(f('data/16-testf.txt'), 23)
        self.assertEqual(f('data/16-testg.txt'), 31)
        self.assertEqual(f('data/16-input.txt'), 936)


if __name__ == "__main__":
    unittest.main()
