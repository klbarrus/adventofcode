#!/usr/bin/env python3
# AdventOfCode 2015 Day 17

import sys
import itertools

#def get_sublists(orig):
#    sublists = [[]]
#    for i in range(len(orig)):
#        for j in range(i+1, len(orig)):
#            subslice = orig[i:j]
#            sublists.append(subslice)
#    return sublists

with open(sys.argv[1]) as f:
    cont = f.readlines()
f.close()
cont = [int(x.strip()) for x in cont]

num150 = 0
mincont = len(cont)
for len in range(0, len(cont)+1):
    for sub in itertools.combinations(cont, len):
        total = sum(sub)
#        print("{} - {}".format(sub, total))
        if total == 150:
            num150 += 1
            if len < mincont:
                mincont = len
        
print("num combinations {}".format(num150))
print("min containers {}".format(mincont))

nummin = 0
for sub in itertools.combinations(cont, mincont):
    total = sum(sub)
    if total == 150:
        nummin += 1

print("num different ways {}".format(nummin))
