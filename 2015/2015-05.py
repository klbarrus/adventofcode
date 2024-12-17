#!/usr/bin/env python3
# AdventOfCode 2015 Day 05

import sys

nice = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip("\n")
        # does not contain ab, cd, pq, xy
        if "ab" in line:
            continue
        if "cd" in line:
            continue
        if "pq" in line:
            continue
        if "xy" in line:
            continue

        # at least 3 vowels
        vowels = 0
        for ch in line:
            if ch in "aeiou":
                vowels += 1
        
        if vowels < 3:
            continue

        # at least one double letter
        double = False
        prev = ''
        for ch in line:
            if ch == prev:
                double = True
            prev = ch

        if not double:
            continue

        nice += 1
        print("{} is nice".format(line))
f.close()

print("Nice strings: {}".format(nice))
