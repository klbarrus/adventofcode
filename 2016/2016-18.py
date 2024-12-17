#!/usr/bin/env python3
# AdventOfCode 2016 Day 18

SAFE = '.'
TRAP = '^'
#INPUT = '..^^.'
#INPUT = '.^^.^.^^^^'
INPUT = '^..^^.^^^..^^.^...^^^^^....^.^..^^^.^.^.^^...^.^.^.^.^^.....^.^^.^.^.^.^.^.^^..^^^^^...^.....^....^.'


def get_next_row(r):
    nr = ''
    # iterate through in triples
    # treat first and last entry as special (safe to left, safe to right)
    triples = [('.', r[0], r[1])]
    for i in zip(r, r[1:], r[2:]):
        triples.append(i)
    triples.append((r[-2], r[-1], '.'))
    for l, c, r in triples:
        if l == c == TRAP and r == SAFE:
            sq = TRAP
        elif l == SAFE and c == r == TRAP:
            sq = TRAP
        elif l == TRAP and c == r == SAFE:
            sq = TRAP
        elif l == c == SAFE and r == TRAP:
            sq = TRAP
        else:
            sq = SAFE
        nr += sq
    return nr


def count_safe(r):
    rv = 0
    for ch in r:
        if ch == SAFE:
            rv += 1
    return rv


for rows in [40, 400000]:
    curr = INPUT
    numsafe = 0
    for i in range(0, rows):
        numsafe += count_safe(curr)
        nextrow = get_next_row(curr)
        curr = nextrow
    print('{} rows, {} safe tiles'.format(rows, numsafe))

