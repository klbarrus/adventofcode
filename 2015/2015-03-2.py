#!/usr/bin/env python3
# AdventOfCode 2015 Day 03 part 2

import sys

loc = [0] * 4 # 0,1 = santa; 2,3 = robo
robo = 0 # 0 = santa, 2 = robo
grid = {}
grid[(loc[0],loc[1])] = 1 # deliver to starting house
with open(sys.argv[1]) as f:
    for line in f:
        for ch in line:
            if ch == '^':
                loc[1 + robo] += 1
            elif ch == '<':
                loc[0 + robo] -= 1
            elif ch == '>':
                loc[0 + robo] += 1
            elif ch == 'v':
                loc[1 + robo] -= 1
            else:
                print("unknown direction")

            if (loc[0 + robo], loc[1 + robo]) in grid:
                grid[(loc[0 + robo], loc[1 + robo])] += 1 # previously visited
            else:
                grid[(loc[0 + robo], loc[1 + robo])] = 1 # new home

            if robo == 0: # switch off
                robo = 2
            else:
                robo = 0
f.close()

num = len(list(grid.keys()))
print("Num houses: {}".format(num))
