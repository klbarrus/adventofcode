#!/usr/bin/env python3
# AdventOfCode 2016 Day 19

import math

INPUT = 3005290

# Josephus problem (see wikipedia)
highbit = math.trunc(math.log2(INPUT))
vl = INPUT - 2**highbit
safepos = 2 * vl + 1
print('part 1: {}'.format(safepos))

p = 3**math.trunc(math.log(INPUT - 1, 3))
safepos = INPUT - p + max(INPUT - 2 * p, 0)
print('part 2: {}'.format(safepos))

