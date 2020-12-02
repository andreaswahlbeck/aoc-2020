#!/usr/bin/env python
from typing import List, Tuple
from itertools import combinations


def find_pairs_of_sum(s: int, start: List[str], elements: int) -> Tuple[int,int]:
    lines = list(map(int, start))
    result = list(filter(lambda x: sum(x) == s,combinations(lines, elements)))
    return result[0]

with open("input.txt") as input:
    i = 1;
    lines = input.readlines()
    matches_of_two = find_pairs_of_sum(2020, lines, 2)
    matches_of_three = find_pairs_of_sum(2020, lines, 3)

    print("answer part1: {}  ({})".format(matches_of_two[0] * matches_of_two[1], str(matches_of_two)))
    print("answer part2: {}  ({})".format(matches_of_three[0] * matches_of_three[1] * matches_of_three[2], str(matches_of_three)))

    