with open('input.txt') as f:
    lines = [int(x.replace("\n", "")) for x in f.readlines()]
    c = 0
    prev = lines[0]
    for cur in lines[1:]:
        if cur > prev:
            c += 1
        prev = cur
print(c)