#!/usr/bin/env python3
# AdventOfCode 2015 Day 06

import sys
import re

# regexp to get the coordinates
rx = re.compile(r'(\d+),(\d+)\s\w+\s(\d+),(\d+)')

grid = {}
with open(sys.argv[1]) as f:
    for line in f:
        ms = rx.search(line)
        if not ms:
            print("No coordinates in {}".format(line))
            continue

        mi = []
        for i in range(1,5):
            mi.append(int(ms.group(i)))

        toggle = False
        light = 0
        if 'toggle' in line:
            toggle = True
        elif 'on' in line:
            light = 1
        elif 'off' in line:
            light = 0
        else:
            print("unrecognized operation in {}".format(line))
            continue

        for x in range(mi[0],mi[2]+1):
            for y in range(mi[1],mi[3]+1):
                if toggle:
                    # if the light isn't in the grid yet, the it is off (default)
                    # so toggle turns it on
                    if not (x,y) in grid:
                        grid[(x,y)] = 1
                    else:
                        grid[(x,y)] = not grid[(x,y)]
                else:
                    grid[(x,y)] = light
f.close()

num = 0
for k,v in grid.items():
    if v == 1:
        num += 1
print("Num lights: {}".format(num))