import sys

def sum(l):
    cur = 0
    for x in l:
        cur += x
    return cur

with open('input.txt') as f:
    lines = [int(x.replace("\n", "")) for x in f.readlines()]
    c = 0
    prev = sum(lines[0: 3])
    for curi in range(3, len(lines)):
        l = lines[curi - 2: curi + 1]
        cur = sum(l)
        if cur > prev:
            c += 1
        prev = cur
print(c)
