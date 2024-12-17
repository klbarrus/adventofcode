#!/usr/bin/env python3
# AdventOfCode 2015 Day 01

import sys

def solve_part1(info):
    floor = 0
    for ch in info:
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
    return floor


def solve_part2(info):
    floor = 0
    currpos = 0
    first = True
    for ch in info:
        if ch == '(':
            floor += 1
            currpos += 1
        elif ch == ')':
            floor -= 1
            currpos += 1
        if (first and (floor == -1)):
            return currpos
    return 0
    

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: {} <datafile>'.format(sys.argv[0]))
        exit(0)

    with open(sys.argv[1]) as f:
        puzzdat = f.readlines()
    f.close()

    for line in puzzdat:
        line.strip()
        part1 = solve_part1(line)
        print('Part 1: {}'.format(part1))

        part2 = solve_part2(line)
        if part2 != 0:
            print('Part 2: {}'.format(part2))
        else:
            print("Didn't enter basement.")        
