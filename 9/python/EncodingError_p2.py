input = list(int(line.strip()) for line in open('../input.txt'))
def findSum(number):
    for i in range(len(input)):
        for j in range(len(input[i:])):
            if sum(input[i:j]) == number:
                return (input[i:j])
sumSet = findSum(23278925)
print(max(sumSet)+min(sumSet))