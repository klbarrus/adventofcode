#!/usr/bin/env python3
# AdventOfCode 2015 Day 24

import sys
import itertools
from operator import mul

def powerset(it):
    s = list(it)
    return itertools.chain.from_iterable(itertools.combinations(s,r) for r in range(len(s)+1))

boxes = []
with open(sys.argv[1]) as f:
    for line in f:
        boxes.append(int(line.strip()))
f.close()

totalweight = sum(boxes)
#goal = totalweight // 3 # part 1
goal = totalweight // 4 # part 2

print("{}".format(boxes))
print("weight {}, goal {}".format(totalweight, goal))

minnum = len(boxes)
minboxes = []

# get all arrangements that add up to the goal weight
group1 = []
minnum = len(boxes)
all = powerset(boxes)
for dist in all:
    weight = sum(dist)
    if weight == goal:
        group1.append(dist)
        if minnum > len(dist):
            minnum = len(dist)
print("{} arrangements available".format(len(group1)))
print("min boxes {}".format(minnum))
#print("{}".format(group1))

# get the arrangements that use the minimum boxes, look for the min QE
nummin = 0
minqe = reduce(mul, boxes, 1)
mindist = ()
for dist in group1:
    if len(dist) == minnum:
        nummin += 1
        qe = reduce(mul, dist, 1)
        if qe < minqe:
            minqe = qe
            mindist = dist
print("min qe {} - {}".format(minqe, mindist))
