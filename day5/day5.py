#!/usr/bin/env python
from math import ceil

def parse_seat_line(line):
   row_part = line[0:7]
   col_part = line[7:10]

   row = find_num(row_part, "F", "B", 0, 127)
   col = find_num(col_part, "L", "R", 0, 7)
   seatid = row * 8 + col
   #print("{}: row {}, column {} seat ID {}".format(line.strip(), row, col, seatid)) 
   return seatid

def find_num(value, lower, upper, low, high):
    if (value == ""):
        return low
    step = value[0]
    middle = ceil((high-low)/2)
    if (step == lower):
        return find_num(value[1:], lower, upper, low, high - middle)
    elif (step == upper):
        return find_num(value[1:], lower, upper, low + middle, high)

def find_available_seat(seats):
    return [x for x in range(seats[0], seats[-1]) if x not in seats] 
    
with open("input.txt") as input:
    lines = input.readlines()
    seats = list(map(parse_seat_line, lines))
    print("max seat: {}".format(max(seats)))
    seats.sort()
    print("avail seat: {}".format(find_available_seat(seats)))