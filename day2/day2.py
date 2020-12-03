#!/usr/bin/env python
import re
from operator import xor


def password_valid(line: str) -> bool:
    p = re.match('([\d]+)-([\d]+) ([\w]): ([\w]+)', line)
    min_occ, max_occ, char_cond, password = p.groups()
    min_occ = int(min_occ)
    max_occ = int(max_occ)
    occ = password.count(char_cond)

    #print("line {}".format(line))
    #print("min: {} max: {} char: {} pass: {}".format(min_occ, max_occ, char_cond, password))
    # part 1
    #return occ >= min_occ and occ <= max_occ
    return xor(password[min_occ-1] == char_cond, password[max_occ-1] == char_cond)


with open("input.txt") as input:
    lines = input.readlines()
    #lines = ['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc']

matches = 0
for line in lines:
    valid = password_valid(line)
    #print("line {} valid: {}".format(line, valid))
    if valid:
        matches += 1

print("number of valid passwords: {}".format(matches))