import re

input = list(line.strip() for line in open('../input.txt'))

def getIndex(index):
    return index%len(input[0])

def treesInSlope(right, down):
    rowIndex=0
    result = 0
    x = right
    for row in input[down:]:
        if(rowIndex%down==0):
            if(row[getIndex(x)]=='#'):
                result+=1
            x+=right
        rowIndex+=1
    return result
print (treesInSlope(1,1) * treesInSlope(3,1) * treesInSlope(5,1) * treesInSlope(7,1)* treesInSlope(1,2))