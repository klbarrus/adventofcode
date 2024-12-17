#!/usr/bin/env python3
# AdventOfCode 2015 Day 03

import sys

x = 0
y = 0
grid = {}
grid[(0,0)] = 1 # deliver to starting house
with open(sys.argv[1]) as f:
    for line in f:
        for ch in line:
            if ch == '^':
                y += 1
            elif ch == '<':
                x -= 1
            elif ch == '>':
                x += 1
            elif ch == 'v':
                y -= 1
            else:
                print("unknown direction")

            if (x,y) in grid:
                grid[(x,y)] += 1
            else:
                grid[(x,y)] = 1         
f.close()

num = len(list(grid.keys()))
print("Num houses: {}".format(num))
