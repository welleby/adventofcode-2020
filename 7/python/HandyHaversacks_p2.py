import re
result = 0

input = list(line.strip() for line in open('../input.txt'))
bags = {}
for row in input:
    itr = re.finditer(r'(^(?P<first>.+?) bags contain )?((((?P<amount>\d+?) (?P<color>.+?)) bags?[,.] ?)|no other bags\.)+?',row)
    bag = ''
    includes = []
    for it in itr:
        if(it.group('first') is not None):
            bag = it.group('first')
        if(it.group('color') is not None):
            includes.append((it.group('color'), it.group('amount')))
    bags[bag] = includes

def traverseBag(currentBag, count, accum):
    if len(bags[currentBag]) == 0:
        return count
    for bag in bags[currentBag]:
        accum += traverseBag(bag[0],int(bag[1]), 0)
    return count + accum*count

print(traverseBag('shiny gold',1,0)-1)