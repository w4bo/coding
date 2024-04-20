with open("01.txt", 'r') as f:
    for line in f.read().replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace('zero', '0').split("\n"):
        first = -1
        last = 0
        sum = 0
        for c in line:
            if c >= '0' and c <= '9':
                print(c)
                if first == -1:
                    first = int(c)
                last = int(c)
            if c == '\n':
                print(c)
                sum += first * 10 + last
    print(sum)