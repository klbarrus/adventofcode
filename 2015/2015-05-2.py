#!/usr/bin/env python3
# AdventOfCode 2015 Day 05 part 2

import sys

# at least one letter which repeats with exactly one letter between them
def spaced_double(line):
    nice = False
    s1 = line[0:len(line)-2]
    s2 = line[2:len(line)]
    for x,y in zip(s1,s2):
        if x == y:
            nice = True
            print("  double found {}".format(x))
 
    return nice

# pair of letters that appear at least twice without overlap
def pair_no_overlap(line):
    nice = False
    i = 0
    while i < len(line)-1:
        pair = line[i:i+2]
        sl = line[0:i]
        sr = line[i+2:]
        # now search new strings for the pair of letters
        if pair in sl:
            nice = True
            print("  pair found {}".format(pair))
            break
        if pair in sr:
            nice = True
            print("  pair found {}".format(pair))
            break
        i += 1

    return nice

nice = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip("\n")
        print("looking at '{}'".format(line))

        res = spaced_double(line)
        if not res:
            print("  no double in {}".format(line))
            continue

        res = pair_no_overlap(line)
        if not res:
            print("  no pair in {}".format(line))
            continue

        nice += 1
        print("*** {} is nice".format(line))
f.close()

print("Nice strings: {}".format(nice))
