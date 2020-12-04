import re
f = open("day4.txt")
passports = []
idx = 0
#Read passports into list of single-line strings; each field is followed by ' '
for line in f:
    if line == '\n':
        idx += 1
    elif len(passports) > idx:
        passports[idx] += line.rstrip('\n') + ' '
    else:
        passports.append(line.rstrip('\n') + ' ')
#Part One
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validOne = 0
passportdicts = []
for passport in passports:
    if all(key in passport for key in keys):
        #Fill list of passport dictionaries for part two; only the ones that contain the 7 required fields
        passportdict = {
            'byr': int(passport.split('byr:')[1].split(' ')[0]),
            'iyr': int(passport.split('iyr:')[1].split(' ')[0]),
            'eyr': int(passport.split('eyr:')[1].split(' ')[0]),
            'hgt': passport.split('hgt:')[1].split(' ')[0],
            'hcl': passport.split('hcl:')[1].split(' ')[0],
            'ecl': passport.split('ecl:')[1].split(' ')[0],
            'pid': passport.split('pid:')[1].split(' ')[0],
        }
        passportdicts.append(passportdict)
        validOne += 1
print(validOne)
#Part Two
validTwo = 0
ecls = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
for passportdict in passportdicts:
    if (
        passportdict['byr'] in range(1920, 2003) and
        passportdict['iyr'] in range(2010, 2021) and
        passportdict['eyr'] in range(2020, 2031) and
        (
            (passportdict['hgt'][-2:] == 'cm' and int(passportdict['hgt'][:-2]) in range(150, 194)) or
            (passportdict['hgt'][-2:] == 'in' and int(passportdict['hgt'][:-2]) in range(59, 77))
        ) and
        re.fullmatch("#[0-9a-f]{6}", passportdict['hcl']) and
        passportdict['ecl'] in ecls and
        re.fullmatch("[0-9]{9}", passportdict['pid'])
    ):
        validTwo += 1
print(validTwo)