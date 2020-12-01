#!/usr/bin/env python
from typing import List, Tuple


def find_pairs_of_sum(summa: int, start: List[str]) -> List[Tuple[int,int]]:
    lines = list(map(int, start))
    sorted_list = list(sorted(lines))
    reversed_list = list(reversed(sorted_list))
    result = []
    i = 0;
    while len(sorted_list):
        print("iteration {}".format(i))
        a = sorted_list.pop()
        rev_work_list = list(filter(lambda x: x <= a, reversed_list))
        print("len of rev work list {}".format(len(rev_work_list)))
        while len(rev_work_list):
            b = rev_work_list.pop()
            print("checking {} and {}".format(a, b))
            if (a + b) > summa:
                print("greater sum")
                break
            if (a + b) == summa:
                print("found match")
                result.append((a,b))
        
        i += 1
    
    return result
    # # for line in lines:
    #     print("{} line number {}".format(line.strip(), i))
    #     i +=  1

with open("input.txt") as input:
    i = 1;
    lines = input.readlines()
    matches = find_pairs_of_sum(2020, lines)

    for match in matches:
        print(match)
        print("answer: {}".format(match[0] * match[1]))

    