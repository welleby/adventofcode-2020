input = set(int(line.strip()) for line in open('../input.txt'))
while input:
    item = input.pop()
    for x in input:
        if (item+x == 2020):
            print(x*item)