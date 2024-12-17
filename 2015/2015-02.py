#!/usr/bin/env python3
# AdventOfCode 2015 Day 02

import sys
import re

def calcslack(l, w, h):
    if (l >= w and l >= h):
        slack = w * h
    elif (w >= l and w >=h):
        slack = l * h
    else:
        slack = l * w
    return slack

def calcribbon(l,w,h):
    if (l >= w and l >= h):
        ribbon = 2 * wi + 2 * hi
    elif (w >= l and w >= h):
        ribbon = 2 * li + 2 * hi
    else:
        ribbon = 2 * li + 2 * wi
    ribbon += (li * wi * hi)
    return ribbon

totalarea = 0
totalribbon = 0
r = re.compile('(\d+)x(\d+)x(\d+)')
with open(sys.argv[1]) as f:
    for line in f:
        #print('{}'.format(line))
        (l,w,h) = r.split(line)[1:4]
        (li,wi,hi) = (int(l),int(w),int(h))
        area = 2*li*wi + 2*wi*hi + 2*li*hi
        slack = calcslack(li, wi, hi)
        totalarea += (area + slack)
        ribbon = calcribbon(li, wi, hi)
        totalribbon += ribbon
f.close()

print("Total area: {}".format(totalarea))
print("Ribbon needed: {}".format(totalribbon))
