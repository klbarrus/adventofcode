#!/usr/bin/env python3
# AdventOfCode 2015 Day 13

import sys
import itertools
from collections import defaultdict

def pairwise(iter):
    a,b = itertools.tee(iter)
    next(b,None)
    return zip(a,b)

def maxhappyseating(arrangements):
    happymax = 0
    happyseating = []
    for seating in arrangements:
        shappy = 0
        for p1,p2 in pairwise(seating):
            shappy += h[p1][p2]
            shappy += h[p2][p1] 
# account for first/last adjacent seating
        shappy += h[seating[0]][seating[-1]]        
        shappy += h[seating[-1]][seating[0]]        
        if shappy > happymax:
            happymax = shappy
            happyseating = seating
    return happymax, happyseating

h = defaultdict(dict)
# read in happiness table
with open(sys.argv[1]) as f:
    for line in f:
        info = line.split()
        name1 = info[0]
        name2 = info[-1].rstrip(".")
        delta = info[2]
        num = int(info[3])
        h[name1][name1] = 0
        if delta == "gain":
            h[name1][name2] = num
        else:
            h[name1][name2] = -num
f.close()

# print table
#for s in sorted(h.keys()):
#    print("{}\t".format(s), end='')
#print("")
#for s in sorted(h.keys()):
#    for d in sorted(h[s].keys()):
#        print("{}\t".format(h[s][d]), end='')
#    print("{}".format(s))

# generate seating arrangements
people = sorted(h.keys())
arrangements = list(itertools.permutations(people))
max, seating = maxhappyseating(arrangements)
print("max happiness {}".format(max))
print("max happiness seating: {}".format(seating))

# include self
for s in sorted(h.keys()):
    h[s]["Me"] = 0
    h["Me"][s] = 0
h["Me"]["Me"] = 0

people = sorted(h.keys())
arrangements = list(itertools.permutations(people))
max, seating = maxhappyseating(arrangements)
print("max happiness {}".format(max))
print("max happiness seating: {}".format(seating))
