#!/usr/bin/env python3
# AdventOfCode 2015 Day 19

import sys
import re

repl = {}
with open(sys.argv[1]) as f:
    for line in f:
        if "=>" in line:
            ele, equ, res = line.strip().split()
            if ele in repl:
                resa = repl[ele]
                resa.append(res)
                repl[ele] = resa
            else:
                repl[ele] = [res]
        elif line:
            med = line.strip()
f.close()

#print("{}".format(repl))
#print("{}".format(med))

# create all molecules from element replacements
moles = []
for ele in repl:
#    print("{}".format(ele))
    locs = [m.start() for m in re.finditer(ele, med)]
#    print("  {}".format(locs))
    for lo in locs:
        for res in repl[ele]:
#            print("  {} -> {} @ {}".format(ele, res, lo))
            moleres = med[:lo] + res + med[lo + len(ele):]
            moles.append(moleres)

# unique-ify list
umoles = []
for mole in moles:
    if mole not in umoles:
        umoles.append(mole)

print("{} unique molecules".format(len(umoles)))

# for part 2, invert the replacement table, sort by length (longest to shortest)
# and replace greedily
invrepl = {}
steps = 0
for k, v in repl.items():
    for i in v:
        invrepl[i] = k
while med != "e":
    for k in sorted(invrepl, key=len, reverse=True):
    #    print("{} -> {}".format(k, invrepl[k]))
        if k in med:
            med = med.replace(k, invrepl[k], 1)
            steps += 1
print("{} steps".format(steps))
