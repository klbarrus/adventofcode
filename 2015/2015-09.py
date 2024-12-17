#!/usr/bin/env python3
# AdventOfCode 2015 Day 9

import sys
import itertools
from collections import defaultdict

def pairwise(iter):
    a,b = itertools.tee(iter)
    next(b,None)
    return zip(a,b)

w = defaultdict(dict)
sdist = 0

# read in distance table
with open(sys.argv[1]) as f:
    for line in f:
        info = line.split()
        c1 = info[0]
        c2 = info[2]
        dist = int(info[4])
        w[c1][c2] = dist
        w[c2][c1] = dist
        w[c1][c1] = 0
        w[c2][c2] = 0
        sdist += dist
f.close()

# print table
for s in sorted(w.keys()):
    print("{}\t".format(s), end='')
print("")

for s in sorted(w.keys()):
    for d in sorted(w[s].keys()):
        print("\t{}".format(w[s][d]), end='')
    print("\t{}".format(s))

# traveling salesman problem
cities = sorted(w.keys())
#print("{}".format(cities))
routes = list(itertools.permutations(cities))
#print("{}".format(routes))

spath = []
lpath = []
ldist = 0

for path in routes:
    pdist = 0
    for c1,c2 in pairwise(path):
#        print("{} to {}".format(c1,c2))
        pdist += w[c1][c2]
    if pdist < sdist:
        # new shortest route found
        spath = path
        sdist = pdist
    if pdist > ldist:
        # new longest route found
        lpath = path
        ldist = pdist

print("shortest path: {}".format(sdist))
print("route is {}".format(spath))
print("longest path: {}".format(ldist))
print("route is {}".format(lpath))
