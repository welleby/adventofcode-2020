input = set(int(line.strip()) for line in open('../input.txt'))
while input:
    item = input.pop()
    subInput = input.copy()
    while subInput:
        subItem = subInput.pop()
        for x in subInput:
            if (item+subItem+x == 2020):
                print(x*item*subItem)