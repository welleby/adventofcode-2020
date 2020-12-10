result = 0
with open('../input.txt', 'r') as file:
    input = file.read()
    groupAnswers = input.split('\n\n')
    for groupAnswer in groupAnswers:
        result += len(set(groupAnswer.replace('\n','')))
print(result)
