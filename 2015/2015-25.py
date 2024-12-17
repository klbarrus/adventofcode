#!/usr/bin/env python3
# AdventOfCode 2015 Day 25

import sys
import re

FIRST = 20151125
MULT = 252533
MOD = 33554393

def lookup(f_row, f_col, debug=False):
    rval = FIRST
    for i in range(1, f_row + f_col):
        for j in range(i, 0, -1):
            c_row = j
            c_col = i-j+1
            if debug:
                print("{},{} - {}".format(c_row, c_col, rval))
            if c_row == f_row and c_col == f_col:
                break
            rval = (rval * MULT) % MOD  
    return rval

p = re.compile(r"row (\d+), column (\d+)")
with open(sys.argv[1]) as f:
    for line in f:
        row, col = p.search(line).groups()
f.close()

code = lookup(int(row),int(col))
print("{},{} - code {}".format(row,col,code))
