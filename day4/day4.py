#!/usr/bin/env python
import re


def parse_passport_lines(lines):
    passports = []
    passports_lines = []
    
    for line in lines:
        if not line.strip():
            # print("creating passport with lines line: {}".format(passports_lines))
            passports.append(create_passport(passports_lines))
            passports_lines.clear()
        else:
            # print("adding line: {}".format(line))
            passports_lines.append(line.strip())
    if passports_lines:
        passports.append(create_passport(passports_lines))

    return passports
        
def create_passport(line):
    pp = {}
    parts = ' '.join(line).split(' ')
    for part in parts:
        k, v = part.split(':')
        pp[k] = v
    print(pp)
    return pp

def valid_passport(passport):
    # needed_keys = ['ecl','pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    # needed_passport = dict(passport)
    # return all(k in needed_keys for k in needed_passport.keys())
    return len(passport) == 8 or (len(passport) == 7 and not 'cid' in passport)

def valid_passport_data(passport):
    return (
        valid_passport(passport) and 
        valid_year(passport['byr'], 1920, 2002) and
        valid_year(passport['iyr'], 2010, 2020) and
        valid_year(passport['eyr'], 2020, 2030) and
        valid_height(passport['hgt']) and
        valid_haircolor(passport['hcl']) and
        valid_eyecolor(passport['ecl']) and
        valid_passportid(passport['pid'])
    )

def valid_passportid(value):
    return re.match('^[0-9]{9,9}$', value)

def valid_eyecolor(value):
    return re.match('^amb|blu|brn|gry|grn|hzl|oth$', value)

def valid_haircolor(value):
    return re.match('^#[0-9a-f]{6,6}$', value)

def valid_height(value):
    p = re.match('(^[\d]+)(cm$|in$){1,1}', value) 
    if (p):
        length, metric = p.groups()
        if metric == 'cm':
            return 150 <= int(length) <= 193
        elif metric == 'in':
            return 59 <= int(length) <= 76
        else:
            return False

def valid_year(value, miny, maxy):
    return (re.match('[\d]{4,4}', value) and (miny <= int(value) <= maxy))

with open("input.txt") as input:
    lines = input.readlines()
    passports = parse_passport_lines(lines)
    print("number of passports {}".format(len(passports)))
    valid_passports = list(filter(lambda p: valid_passport(p), passports))
    print("number of valid passports: {}".format(len(valid_passports)))
    valid_data_passports = list(filter(lambda p: valid_passport_data(p), passports))
    print("number of valid data passports: {}".format(len(valid_data_passports)))