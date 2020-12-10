result = 0
with open('../input.txt', 'r') as file:
    input = file.read()
    groupAnswers = input.split('\n\n')
    for groupAnswer in groupAnswers:
        individualAnswers = groupAnswer.split('\n')
        answersDict = {}
        for individualAnswer in individualAnswers:
            for yes in individualAnswer:
                if answersDict.get(yes):
                    answersDict[yes]+=1
                else:
                    answersDict[yes]=1
        for key,val in answersDict.items():
            if val == len(individualAnswers):
                result+=1
print(result)
