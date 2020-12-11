import re
result = 0

input = list(line.strip() for line in open('../input.txt'))
numberPattern = re.compile(r'.* \+?(-?\d+)$')


def loopDiLoop():
    i=0
    acc=0
    visited=set()
    while i<len(input):
        print(input[i])
        if i in visited:
            print(acc)
            return
        visited.add(i)
        nmbr = numberPattern.match(input[i])
        if input[i].startswith('acc'):
            acc+=int(nmbr.group(1))
        if input[i].startswith('jmp'):
            i += int(nmbr.group(1))
        else:
            i+=1

loopDiLoop()