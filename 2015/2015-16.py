#!/usr/bin/env python3
# AdventOfCode 2015 Day 16

import sys
from operator import ge, le

mysterysue = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

part2 = {
    'cats': ge,
    'trees': ge,
    'pomeranians': le,
    'goldfish': le,
}

def scoresue(items, values):
#    match = 0
    for i, j in zip(items, values):
        if mysterysue[i] != j:
            return False
    return True
#            match += 1
#    return match

def scoresue2(items, values):
#    match = 0
    for special, oper in part2.items():
        if special in items:
            idx = items.index(special)
            num = values[idx]
            items.pop(idx)
            values.pop(idx)
#            print("{} {}".format(special,num))
            if not oper(num, mysterysue[special]):
                return False
    return scoresue(items, values)
#                match += 1
#    match += scoresue(items, values)
#    return match

#ms1 = 0
#mn1 = 0
#ms2 = 0
#mn2 = 0
with open(sys.argv[1]) as f:
    for line in f:
        sueinfo = line.split()
        suenum = sueinfo[1].rstrip(':')
        items = []
        vals = []
        for i in range(2,len(sueinfo),2):
            items.append(sueinfo[i].rstrip(':'))
            vals.append(int(sueinfo[i+1].rstrip(',')))
#        print("items {}".format(items))
#        print("vals {}".format(vals))

        match = scoresue(items, vals)
        if match:
            print("Aunt Sue part 1 - {}".format(suenum))
#        if match > mn1:
#            mn1 = match
#            ms1 = suenum
#        
        match = scoresue2(items, vals)
        if match:
            print("Aunt Sue part 2 - {}".format(suenum))
#        if match > mn2:
#            mn2 = match
#            ms2 = suenum
f.close()

#print("aunt sue {}, max match {}".format(ms1, mn1))
#print("aunt sue {}, max match {}".format(ms2, mn2))
