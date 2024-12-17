#!/usr/bin/env python3
# AdventOfCode 2015 Day 06 part 2

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
        on = False
        if 'toggle' in line:
            toggle = True
        elif 'on' in line:
            on = True
        elif 'off' in line:
            on = False
        else:
            print("unrecognized operation in {}".format(line))
            continue

        for x in range(mi[0],mi[2]+1):
            for y in range(mi[1],mi[3]+1):
                if toggle:
                    # if the light isn't in the grid yet, the it is off (default)
                    # so toggle turns it on from 0 to 2
                    if not (x,y) in grid:
                        grid[(x,y)] = 2
                    else:
                        grid[(x,y)] += 2
                else:
                    if not (x,y) in grid:
                        grid[(x,y)] = 0

                    if on:
                        grid[(x,y)] += 1
                    else:
                        grid[(x,y)] -= 1
                        if grid[(x,y)] < 0:
                            grid[(x,y)] = 0
f.close()

bright = 0
for k,v in grid.items():
    bright += v
print("Brightness: {}".format(bright))