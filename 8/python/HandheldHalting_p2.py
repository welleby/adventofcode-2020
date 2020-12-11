import re
result = 0

input = list(line.strip() for line in open('../input.txt'))
numberPattern = re.compile(r'.* \+?(-?\d+)$')


def loopDiLoop(input):
    i=0
    acc=0
    visited=set()
    while i<len(input):
        if i in visited:
            return False
        visited.add(i)
        nmbr = numberPattern.match(input[i])
        if input[i].startswith('acc'):
            acc+=int(nmbr.group(1))
        if input[i].startswith('jmp'):
            i += int(nmbr.group(1))
        else:
            i+=1
    print(acc)
    return True

def fixDiLoop():
    i=0
    while i<len(input):
        tampered = input.copy()
        if input[i].startswith('jmp'):
            tampered[i] = tampered[i].replace('jmp','nop')
        if input[i].startswith('nop'):
            tampered[i] = tampered[i].replace('nop','jmp')
        if loopDiLoop(tampered):
            return
        i+=1

fixDiLoop()