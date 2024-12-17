#!/usr/bin/env python3
# AdventOfCode 2015 Day 18

import sys
import copy

def count_alive(grid):
    num = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]:
                num += 1
    return num

def count_neighbors(grid, x, y, debug=False):
    if debug:
        print("checking {},{}".format(x,y))
    num = 0
    size = len(grid)
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0:
                continue
            if i > size-1 or j > size-1:
                continue
            if i == x and j == y:
                continue
            if grid[i][j]:
                num += 1
                if debug:
                    print("  alive {},{}".format(i,j))
    return num

def game_of_life(grid, gens, part2=False, debug=False):
    size = len(grid)
    for steps in range(gens):
        if part2:
            grid[0][0] = 1
            grid[0][size-1] = 1
            grid[size-1][0] = 1
            grid[size-1][size-1] = 1
        next = copy.deepcopy(grid)
        for i in range(size):
            for j in range(size):
                num = count_neighbors(grid, i, j, debug)
                if debug:
                    print("  {},{} - {} neighbors".format(i,j,num))
                if grid[i][j]:
                    if num == 2 or num == 3:
                        next[i][j] = 1
                    else:
                        next[i][j] = 0
                else:
                    if num == 3:
                        next[i][j] = 1
                    else:
                        next[i][j] = 0
        if part2:
            next[0][0] = 1
            next[0][size-1] = 1
            next[size-1][0] = 1
            next[size-1][size-1] = 1
        grid = next
        if debug:
            print("step {}".format(grid))
    return next

sample_grid = [
    [0,1,0,1,0,1],
    [0,0,0,1,1,0],
    [1,0,0,0,0,1],
    [0,0,1,0,0,0],
    [1,0,1,0,0,1],
    [1,1,1,1,0,0]
]

#sample_out = game_of_life(sample_grid, 4, False, False)
#print("{}".format(sample_grid))
#print("{} on in sample".format(count_alive(sample_out)))

#sample_out = game_of_life(sample_grid, 5, True, False)
#print("{}".format(sample_grid))
#print("{} on in sample part 2".format(count_alive(sample_out)))

lights = []
with open(sys.argv[1]) as f:
    for line in f:
        lrow = [{'#':1,'.':0}[i] for i in line.strip()]
        lights.append(lrow)
f.close()

lights_out = game_of_life(lights, 100, False, False)
print("{} on".format(count_alive(lights_out)))

lights_out = game_of_life(lights, 100, True, False)
print("{} on part 2".format(count_alive(lights_out)))
