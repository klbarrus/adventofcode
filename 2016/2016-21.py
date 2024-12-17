#!/usr/bin/env python3
# AdventOfCode 2016 Day 21

import sys
import re
import itertools


def scramble(password, inst):
    pw = list(password)
    for line in inst:
        m = re.match(r'swap position (\d+) with position (\d+)', line)
        if m:
            a = int(m.group(1))
            b = int(m.group(2))
            pw[a], pw[b] = pw[b], pw[a]
            continue

        m = re.match(r'swap letter (\w) with letter (\w)', line)
        if m:
            a = pw.index(m.group(1))
            b = pw.index(m.group(2))
            pw[a], pw[b] = pw[b], pw[a]
            continue

        m = re.match(r'rotate left (\d+)', line)
        if m:
            a = int(m.group(1))
            pw = pw[a:] + pw[:a]
            continue

        m = re.match(r'rotate right (\d+)', line)
        if m:
            a = int(m.group(1))
            pw = pw[-a:] + pw[:-a]
            continue

        m = re.match(r'rotate based on position of letter (\w)', line)
        if m:
            a = pw.index(m.group(1))
            b = (a + 1 + (a >= 4)) % len(pw)
            pw = pw[-b:] + pw[:-b]
            continue

        m = re.match(r'reverse positions (\d+) through (\d+)', line)
        if m:
            a = int(m.group(1))
            b = int(m.group(2))
            pw[a:b + 1] = pw[a:b + 1][::-1]
            continue

        m = re.match(r'move position (\d+) to position (\d+)', line)
        if m:
            a = int(m.group(1))
            b = int(m.group(2))
            pw[a:a + 1], pw[b:b] = [], pw[a]
            continue
    return ''.join(pw)


inst =[]
with open(sys.argv[1]) as f:
    inst = list(f)
f.close()

part1 = scramble('abcdefgh', inst)
print('part 1: {}'.format(part1))

for perm in itertools.permutations('abcdefgh'):
    scram = scramble(perm, inst)
    if scram == 'fbgdceah':
        print('part 2: {}'.format(''.join(perm)))
        break

