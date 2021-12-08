import unittest
import sys

# Infer the schema from the input. Map it to a well known schema
def schema(input):
    #  dddd
    # e    a
    # e    a
    #  ffff
    # g    b
    # g    b
    #  cccc
    res = {}
    
    curres = {}
    for o in input: # get the heatmap of all segments
        for x in o:
            curres[x] = 1 + curres.get(x, 0)

    todelete = []
    for k, v in curres.items():
        if v == 4:
            res[k] = "g"
            todelete.append(k)
        elif v == 6:
            res[k] = "e"
            todelete.append(k)
        elif v == 9:
            res[k] = "b"
            todelete.append(k)
    
    if len(todelete) != 3:
        sys.exit(1)

    for k in todelete:
        del curres[k]

    for o in input: # this is a 1
        if len(o) == 2:
            for x in o:
                if x in curres:
                    res[x] = "a"
                    del curres[x]

    for o in input: # this is a 7
        if len(o) == 3:
            for x in o:
                if x in curres:
                    res[x] = "d"
                    del curres[x]

    for o in input: # this is a 4
        if len(o) == 4:
            for x in o:
                if x in curres:
                    res[x] = "f"
                    del curres[x]

    if len(curres) != 1:
        sys.exit(1)
    for k, v in curres.items():
        res[k] = "c"

    return res

def map(x):
    r = "?"
    if len(x) == 7:
        r = 8
    elif len(x) == 5:
        if "a" not in x and "g" not in x:
            r = 5
        elif "e" not in x and "b" not in x:
            r = 2
        elif "e" not in x and "g" not in x:
            r = 3
        else:
            print("Unknown " + str(x))
    elif len(x) == 3:
        r = 7
    elif len(x) == 6:
        if "a" not in x:
            r = 6
        elif "g" not in x:
            r = 9
        elif "f" not in x:
            r = 0
        else:
            print("Unknown " + str(x))
    elif len(x) == 4:
        r = 4
    elif len(x) == 2:
        r = 1
    else:
        print("Unknown " + str(x))
    return str(r)



def f(filename):
    with open(filename) as f:
        lines = [[y.split(" ") for y in x.strip().split(" | ")] for x in f.readlines()]  # read the 
        
        sum = 0
        for line in lines:
            input = line[0]
            output = line[1]
            mapping = schema(input)
            output = [''.join([mapping[y] for y in x]) for x in output]
            output = ''.join([map(x) for x in output])
            output = int(output)
            sum += output
        return sum


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(f('data/08-test.txt'), 61229)
        self.assertEqual(f('data/08-testa.txt'), 5353)
        self.assertEqual(f('data/08-input.txt'), 940724)

if __name__ == "__main__":
    unittest.main()
