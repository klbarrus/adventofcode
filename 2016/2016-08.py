#!/usr/bin/env python3
# AdventOfCode 2016 Day 08

import sys
import re
import numpy as np

SCREEN_WIDE = 50
SCREEN_TALL = 6
p_rect = re.compile(r'rect (\d+)x(\d+)')
p_col  = re.compile(r'rotate column x=(\d+) by (\d+)')
p_row  = re.compile(r'rotate row y=(\d+) by (\d+)')


def create_rect(grid, xc, yc):
    o = np.ones((xc, yc), dtype=int)
    grid[0:xc, 0:yc] = o
    return grid


def rotate_col(grid, col, off):
    gt = np.transpose(grid)
    ac = gt[col:col+1, :]
    ac = np.roll(ac, off)
    gt[col:col+1, :] = ac
    grid = np.transpose(gt)
    return grid


def rotate_row(grid, row, off):
    ar = grid[row:row+1, :]
    ar = np.roll(ar, off)
    grid[row:row+1, :] = ar
    return grid


screen = np.zeros((SCREEN_TALL, SCREEN_WIDE), dtype=int)
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()

        m = p_rect.match(line)
        if m:
            nc = int(m.group(1))
            nr = int(m.group(2))
            screen = create_rect(screen, nr, nc)
            continue

        m = p_col.match(line)
        if m:
            c = int(m.group(1))
            off = int(m.group(2))
            screen = rotate_col(screen, c, off)
            continue

        m = p_row.match(line)
        if m:
            r = int(m.group(1))
            off = int(m.group(2))
            screen = rotate_row(screen, r, off)
            continue
f.close()
on = np.count_nonzero(screen)
print('on: {}'.format(on))

# print subarrays corresponding to letters
for i in range(0, 10):
    letter = screen[0:6, i*5:(i+1)*5]
    print('{}'.format(letter))

