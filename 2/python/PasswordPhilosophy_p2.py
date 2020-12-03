import re
input = list(line.strip() for line in open('../input.txt'))
result = 0
for row in input:
    match = re.match(r'^(\d+)-(\d+) (.): (.+)$',row)
    index1 = int(match.group(1))-1
    index2 = int(match.group(2))-1
    letter = match.group(3)
    password = match.group(4)
    if (re.match(rf'^(.{{{index1}}}{letter})',password) is not None) ^ (re.match(rf'^(.{{{index2}}}{letter})',password) is not None):
        result+=1
print(result)