import re

class Passport():
    def __init__(self, byr,iyr,eyr,hgt,hcl,ecl,pid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
    def __str__(self):
        return f'byr: {self.byr}, iyr: {self.iyr}, eyr: {self.eyr}, hgt: {self.hgt}, hcl: {self.hcl}, ecl: {self.ecl}, pid: {self.pid}'
    def isValid(self):
        if(self.byr is None):
            return False
        if(self.iyr is None):
            return False
        if(self.eyr is None):
            return False
        if(self.hgt is None):
            return False
        if(self.hcl is None):
            return False
        if(self.ecl is None):
            return False
        if(self.pid is None):
            return False
            

        heightMatch = re.match(r'((?P<cm>\d+)cm)|((?P<in>\d+)in)',self.hgt)
        hgtOk = False
        if heightMatch is None:
            return False
        elif heightMatch.group('cm') is not None:
            hgtOk = int(heightMatch.group('cm')) >= 150 and \
                int(heightMatch.group('cm')) <=193
        elif heightMatch.group('in') is not None:
            hgtOk = int(heightMatch.group('in')) >= 59 and \
                int(heightMatch.group('in')) <=76
        else:
            return False

        return int(self.byr) >= 1920 and int(self.byr)<=2002 and \
            int(self.iyr) >= 2010 and int(self.iyr)<=2020 and \
            int(self.eyr) >= 2020 and int(self.eyr)<=2030 and \
            hgtOk and \
            re.match(r'^#[0-9a-f]{6}$',self.hcl) is not None and \
            re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$',self.ecl) is not None and \
            re.match(r'^\d{9}$',self.pid) is not None

###
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
###

def parsePassport(passportString):
    m = re.match(r'((byr:(?P<byr>.+?)|iyr:(?P<iyr>.+?)|eyr:(?P<eyr>.+?)|hgt:(?P<hgt>.+?)|hcl:(?P<hcl>.+?)|ecl:(?P<ecl>.+?)|pid:(?P<pid>.+?)|cid:(?P<cid>.+?))([ \n]|$))+',passportString)
    print(passportString)
    print(m.groupdict())
    return Passport(m.group('byr'), m.group('iyr'), m.group('eyr'), m.group('hgt'), m.group('hcl'), m.group('ecl'), m.group('pid'))

result = 0
with open('../input.txt', 'r') as file:
    input = file.read()
    passportStrings = input.split('\n\n')
    passportPattern = re.compile(r'(byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:)')
    for passportString in passportStrings:
        if (len(passportPattern.findall(passportString.replace('\n',' '))) == 7) :
            passport = parsePassport(passportString.replace('\n',' '))
            print(passport)
            if(passport.isValid()):
                result+=1
print(result)
