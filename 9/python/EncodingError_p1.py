input = list(int(line.strip()) for line in open('../input.txt'))

def isValid(currSet, number):
    i=0
    while i< len(currSet):
        j=i+1
        while j< len(currSet):
            if ((currSet[i]+currSet[j]) == number):
                return True
            j+=1
        i+=1
    return False
def xmas(preambleSize):
    currentList = list()
    for number in input[:preambleSize]:
        currentList.append(number)
    for number in input[preambleSize:]:
        if(not isValid(currentList,number)):
            print(number)
            return
        currentList.pop(0)
        currentList.append(number)

xmas(25)