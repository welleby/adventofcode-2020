import re

input = list(line.strip() for line in open('../input.txt'))

def getIndex(index):
    return index%len(input[0])

result = 0
x=3
for row in input[1:]:
    if(row[getIndex(x)]=='#'):
        result+=1
    x+=3
print(result)