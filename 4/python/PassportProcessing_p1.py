import re
result = 0
with open('../input.txt', 'r') as file:
    input = file.read()
    passportStrings = input.split('\n\n')
    passportPattern = re.compile(r'(byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:)')
    for passportString in passportStrings:
        if (len(passportPattern.findall(passportString.replace('\n',' '))) == 7) :
            result+=1
print(result)