#!/usr/bin/env python3
# AdventOfCode 2015 Day 20

from math import sqrt

NUM_PRESENTS = 29000000

def factors(n):
    f = set()
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            f.add(i)
            f.add(n//i)
    return sorted(f)

done = False
hnum = 1
while not done:
    elves = factors(hnum)
    pres = 10 * sum(elves)
#    print("house {}, elves{}, presents {}".format(hnum, elves, pres))
    if pres >= NUM_PRESENTS:
        done = True
        break
    hnum += 1
print("house number {}".format(hnum))

done = False
hnum = 1
while not done:
    elves = factors(hnum)
    elves = [e for e in elves if e * 50 >= hnum]
    pres = 11 * sum(elves)
#    print("house {}, elves{}, presents {}".format(hnum, elves, pres))
    if pres >= NUM_PRESENTS:
        done = True
        break
    hnum += 1
print("house number {}".format(hnum))
