from enum import Enum
from copy import copy, deepcopy
input = list(line.strip() for line in open('../input.txt'))

class Spot(Enum):
    empty = 'L'
    occupied = '#'
    floor = '.'
    @staticmethod
    def getSpot(char):
        if char == '.':
            return Spot.floor
        elif char == 'L':
            return Spot.empty
        elif char == '#':
            return Spot.occupied
        return None

class Seat():
    @staticmethod
    def getSurroundingSeats(x, y):
        if x>0 and y>0:
            return [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
        elif y==0 and x == 0:
            return [(x+1,y),(x,y+1),(x+1,y+1)]
        elif y==0 and x>0:
            return [(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
        elif x==0 and y>0:
            return [(x,y-1),(x+1,y-1),(x+1,y),(x,y+1),(x+1,y+1)]

    @staticmethod
    def canOccupy(currentSeatings, x, y):
        for seat in Seat.getSurroundingSeats(x,y):
            if Seat.currentSeatState(currentSeatings,seat[0],seat[1]) == Spot.occupied:
                return False
        return True
    @staticmethod
    def shouldLeave(currentSeatings, x, y):
        surroundingOccupied = 0
        for seat in Seat.getSurroundingSeats(x,y):
            if Seat.currentSeatState(currentSeatings,seat[0],seat[1]) == Spot.occupied:
                surroundingOccupied+=1
        return surroundingOccupied>=4
    @staticmethod
    def newSeatState(currentSeatings, x, y):
        currSeatState = Seat.currentSeatState(currentSeatings,x,y)
        if currSeatState == Spot.floor:
            return Spot.floor
        elif currSeatState == Spot.empty:
            return Spot.occupied if Seat.canOccupy(currentSeatings,x,y) else currSeatState
        elif currSeatState == Spot.occupied:
            return Spot.empty if Seat.shouldLeave(currentSeatings,x,y) else currSeatState
    @staticmethod
    def currentSeatState(currentSeatings, x, y):
        try: 
            return Spot.getSpot(currentSeatings[y][x])
        except IndexError as error:
            return None

def runSeatRound(currentInput):
    rowIndex = 0
    nextInput = deepcopy(currentInput)
    while rowIndex < len(currentInput):
        currentRow = currentInput[rowIndex]
        prevRow = []
        nextRow = []
        if rowIndex>=1:
            prevRow=currentInput[rowIndex-1]
        if rowIndex<len(currentInput)-1:
            nextRow=currentInput[rowIndex+1]

        colIndex=0
        while colIndex < len(currentRow):
            nextInput[rowIndex][colIndex] = Seat.newSeatState(currentInput,colIndex,rowIndex).value
            colIndex+=1
        rowIndex+=1
    return nextInput

def mapInput():
    return [[char for char in row] for row in input]

def countOccupiedSeats(currentInput):
    occupiedSeats = 0
    for row in currentInput:
        for seat in row:
            if Spot.getSpot(seat) == Spot.occupied:
                occupiedSeats+=1
    return occupiedSeats

def runToHalt():
    currentInput = mapInput()
    previousInput = deepcopy(currentInput)
    i = 0
    while True:
        previousInput = deepcopy(currentInput)
        currentInput = runSeatRound(currentInput)
        if currentInput == previousInput:
            break
        i+=1

    print(f'Runs: {i}')
    print(currentInput)
    print(countOccupiedSeats(currentInput))


runToHalt()
# print(runSeatRound(mapInput()))
# print(runSeatRound(runSeatRound(mapInput())))

