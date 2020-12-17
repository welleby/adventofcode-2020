input = list(int(line.strip()) for line in open('../input.txt'))

def isPermutable(i):
    currJolt = input[i]
    prevJump = 0
    nextJump = 0
    if i-1 >= 0:
        prevJolt = input[i-1]
        prevJump = currJolt - prevJolt
    if i+1 < len(input):
        nextJolt = input[i+1]
        nextJump = nextJolt - currJolt
    return prevJump == 1 and nextJump == 1

def getPermutations(inRow):
    if inRow == 1:
        return 2
    if inRow == 2:
        return 4
    if inRow == 3:
        return 7
    return 2^inRow - 2^(inRow-2)

def identifyPermutations():
    input.append(0)
    input.sort()
    permutations = 1
    i = 0
    while i < len(input):
        permutablesInRow = 0
        if isPermutable(i):
            while isPermutable(i):
                permutablesInRow+=1
                i+=1
            permutations*=getPermutations(permutablesInRow)
        i+=1
    return permutations


print(identifyPermutations())

# (0), 1, 1, 1, 1, 3, 1, 1, 1,  1,  3,  3,  1,  1,  1,  3,  1,  1,  3,  3,  1,  1,  1,  1,  3,  1,  3,  3,  1,  1,  1,  1,  3    Prev
# (0), 1, 1, 1, 3, 1, 1, 1, 1,  3,  3,  1,  1,  1,  3,  1,  1,  3,  3,  1,  1,  1,  1,  3,  1,  3,  3,  1,  1,  1,  1,  3   0    Next
#  O   M  M  M  D  D  M  M  M   D   D   D   M   M   D   D   M   D   D   D   M   M   M   D   D   D   D   D   M   M   M   D   D
#  /      7     /  /     7      /   /   /     4     /   /   2   /   /   /       7       /   /   /   /   /       7           /
# (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
#  -   -  X  X  -  -  X  X  O   -   -   -   X   X   -   -   X   -   -   -   X   X   O   -   -   -   -   -   X   X   O   -    -

# 1. "Doubble-threes" where two threes are next to eachother can never be removed. "Threes", either previous or next
# 2. "Ones" are always optional IF there are no more than 2 in a row
# 3. "MultiOnes" where there are more than two 1s in a row can be optional as long as there is "reach" to the next joltage
#     MultiOnes have 2^X - 2^(X-2) permutations (except for 3, 1,2,3 which has 2, 4, 7 respectivly)
#         Identify MultiOnes by "DoubleOnes" in row
# #example2: 19208