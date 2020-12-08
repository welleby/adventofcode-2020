from binarytree import tree, bst, heap
import re
input = list(line.strip() for line in open('../input.txt'))

def binSearch(string):
    string = string.replace('F', '0')
    string = string.replace('L', '0')
    string = string.replace('B', '1')
    string = string.replace('R', '1')
    return int(string,2)

maxId = 0
for row in input:
    currId = binSearch(row[0:7]) * 8 + binSearch(row[7:])
    if(currId>maxId):
        maxId = currId
print(maxId)
