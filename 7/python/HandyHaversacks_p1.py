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

def traverseBag(currentBag,isGold=False):
    if currentBag == 'shiny gold':
        return True
    for bag in bags[currentBag]:
        isGold = isGold or traverseBag(bag[0],isGold)
    return isGold

def traverseBags():
    result = 0
    for bag in bags:
        if traverseBag(bag):
            result+=1
    return result-1 # remove the original shiny gold

print(traverseBags())