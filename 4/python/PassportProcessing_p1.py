import re

class Passport():
    def __init__(self, byr,iyr,eyr,hgt,hcl,ecl,pid,cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid
with open('../input.txt', 'r') as file:
    input = file.read()
    passportStrings = input.split('\n\n')
