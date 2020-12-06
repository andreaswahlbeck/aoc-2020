#!/usr/bin/env python

def extract_groups_from_file(input):
    groups = []
    current_group = []
    while(True):
        line = input.readline()
        if line == "" or line == "\n":
            groups.append(current_group.copy())
            current_group.clear()
            if line == "":
                break
        else:
            current_group.append(line.strip())
        
    return groups

def uniq_yes_answers(group):
    y = set()
    for p in group:
        y.update(list(p))

    return y

def all_yes_answer_in_groups(groups):
    r = []
    for g in groups:
        all_yes = set()
        all_yes.update(uniq_yes_answers(g))
        y = all_yes.intersection(*[set(x) for x in g])
        r.append(y)
    
    return r
    

with open("input.txt") as input:
    groups = extract_groups_from_file(input)
    u_yes_a = list(map(lambda g: uniq_yes_answers(g), groups))
    print("part 1 unique yes anserws sum: {}".format(sum(map(lambda a: len(a),u_yes_a))))
    
    common_yes_anserws_per_group = all_yes_answer_in_groups(groups)
    print("part 2 common yes answers sum: {}".format(sum(map(lambda a: len(a), common_yes_anserws_per_group))))
