#!/usr/bin/env python3
# AdventOfCode 2016 Day 11

FLOORS = 4

def get_num_moves(items):
    rv = 0
    for floor in range(1, FLOORS):
        sum_items = sum(items[0:floor])
        rv += 2 * (sum_items - 1) - 1
    return rv


items_1 = [4,5,1,0]
print('part 1: {}'.format(get_num_moves(items_1)))
items_2 = [8,5,1,0]
print('part 2: {}'.format(get_num_moves(items_2)))

