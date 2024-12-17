#!/usr/bin/env python3
# AdventOfCode 2016 Day 03

import sys


def check_triangle(x):
    # print('{}'.format(x))
    rv = 0
    a = int(x[0])
    b = int(x[1])
    c = int(x[2])
    if a + b > c and a + c > b and b + c > a:
        rv = 1
    return rv


with (open(sys.argv[1])) as f:
    poss = 0
    for line in f:
        tri = line.split()
        if len(tri) == 0:
            break
        poss += check_triangle(tri)
    print('possible: {}'.format(poss))
f.close()

with (open(sys.argv[1])) as f:
    poss = 0
    lr = 0
    tri1 = []
    tri2 = []
    tri3 = []
    for line in f:
        tri = line.split()
        if len(tri) == 0:
            break
        lr += 1
        tri1.append(tri[0])
        tri2.append(tri[1])
        tri3.append(tri[2])
        if lr == 3:
            poss += check_triangle(tri1)
            poss += check_triangle(tri2)
            poss += check_triangle(tri3)
            lr = 0
            tri1 = []
            tri2 = []
            tri3 = []
    print('possible: {}'.format(poss))
f.close()
