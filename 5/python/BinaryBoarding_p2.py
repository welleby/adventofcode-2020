from binarytree import tree, bst, heap
import re
input = list(line.strip() for line in open('../input.txt'))

def binSearch(string):
    string = string.replace('F', '0')
    string = string.replace('L', '0')
    string = string.replace('B', '1')
    string = string.replace('R', '1')
    return int(string,2)

seats = []
for row in input:
    currId = binSearch(row[0:7]) * 8 + binSearch(row[7:])
    seats.append(currId)
seats.sort()


def getAllSeats():
    result = []
    for i in range(48,115):
        for j in range(8):
            result.append(i*8+j)
    return result

def Diff(li1, li2):
    return (list(list(set(li1)-set(li2))))

print(Diff(getAllSeats(),seats))
