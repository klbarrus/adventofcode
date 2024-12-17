#!/usr/bin/env python3
# AdventOfCode 2015 Day 12

import json
import sys

def do_sum(item, skip_red = False):
    if isinstance(item, int):
        return item

    if isinstance(item, str):
        return 0

    if isinstance(item, list):
        sum = 0
        for i in item:
            sum += do_sum(i, skip_red)
        return sum

    if isinstance(item, dict):
        sum = 0
        if skip_red and 'red' in item.values():
            return 0
        for i in item.values():
            sum += do_sum(i, skip_red)
        return sum


with open(sys.argv[1]) as f:
    d = json.load(f)

print("sum: {}".format(do_sum(d)))
print("sum skipping red: {}".format(do_sum(d, True)))
