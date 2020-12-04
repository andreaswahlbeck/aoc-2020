#!/usr/bin/env python

def init_map(lines):
    m = []
    for line in lines:
        m.append([char for char in line.strip()])
    
    return m

def traverse_map(m,sy,sx):
    x = 1
    y = 1
    hits = 0

    goal_y = len(m)
    positions = []
    x_len = len(m[0])

    while y < goal_y:
        x += sx
        y += sy

        x_pos = (x % x_len)

        if m[y-1][x_pos-1] == '#':
            mark = 'X'
            hits += 1
        else:
            mark = '0'
        
        positions.append((x,y,mark))

    return hits

with open("input.txt") as input:
    lines = input.readlines()
    
    m = init_map(lines)
    
    hits = traverse_map(m,1,3)
    print("part one you hit {} trees".format(hits))
    

    hits1 = traverse_map(m,1,1)
    hits2 = traverse_map(m,1,3)
    hits3 = traverse_map(m,1,5)
    hits4 = traverse_map(m,1,7)
    hits5 = traverse_map(m,2,1)

    print("you hit {} trees".format(hits1))
    print("you hit {} trees".format(hits2))
    print("you hit {} trees".format(hits3))
    print("you hit {} trees".format(hits4))
    print("you hit {} trees".format(hits5))

    print("Part 2 answer: {}".format(hits1*hits2*hits3*hits4*hits5))

