import re
input = list(line.strip() for line in open('../input.txt'))
result = 0
for row in input:
    match = re.match(r'^(\d+)-(\d+) (.): (.+)$',row)
    pattern = re.compile(match.group(3))
    mini = int(match.group(1))
    maxi = int(match.group(2))
    matchingChars = len(pattern.findall(match.group(4)))
    if(matchingChars >= mini and matchingChars <= maxi):
        result+=1
print(result)