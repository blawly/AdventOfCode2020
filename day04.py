import re
with open('input/day04.txt') as f:
    passports = []
    idx = 0
    for line in f:
        if line == '\n':
            idx += 1
        elif len(passports) > idx:
            passports[idx] += line.rstrip('\n') + ' '
        else:
            passports.append(line.rstrip('\n') + ' ')

# Part One
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validOne = 0
passportdicts = []
for passport in passports:
    if all(key in passport for key in keys):
        validOne += 1
        # Fill list of passport dictionaries for part two; only the ones that contain the 7 required fields are relevant
        passportdict = dict((key, (passport.split('{}:'.format(key))[1].split(' ')[0])) for key in keys)
        passportdicts.append(passportdict)
print(validOne)

# Part Two
validTwo = 0
for passportdict in passportdicts:
    if (
        int(passportdict['byr']) in range(1920, 2003) and
        int(passportdict['iyr']) in range(2010, 2021) and
        int(passportdict['eyr']) in range(2020, 2031) and
        (
            (passportdict['hgt'][-2:] == 'cm' and int(passportdict['hgt'][:-2]) in range(150, 194)) or
            (passportdict['hgt'][-2:] == 'in' and int(passportdict['hgt'][:-2]) in range(59, 77))
        ) and
        re.fullmatch("#[0-9a-f]{6}", passportdict['hcl']) and
        passportdict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and
        re.fullmatch("[0-9]{9}", passportdict['pid'])
    ):
        validTwo += 1
print(validTwo)