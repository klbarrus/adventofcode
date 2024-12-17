#!/usr/bin/env python3
# AdventOfCode 2016 Day 12

import sys
import re

#VARS = {}
VARS = {'c': 1}
ip = 0

with open(sys.argv[1]) as f:
    prog = f.read().splitlines()
f.close()

while ip < len(prog):
    inst = prog[ip]

    m = re.match('cpy (\d+) (\w+)', inst)
    if m:
        VARS[m.group(2)] = int(m.group(1))
        ip += 1
        continue

    m = re.match('cpy (\w+) (\w+)', inst)
    if m:
        VARS[m.group(2)] = VARS[m.group(1)]
        ip += 1
        continue

    m = re.match('inc (\w+)', inst)
    if m:
        VARS[m.group(1)] += 1
        ip += 1
        continue

    m = re.match('dec (\w+)', inst)
    if m:
        VARS[m.group(1)] -= 1
        ip += 1
        continue

    m = re.match('jnz (-?\d+) (-?\d+)', inst)
    if m:
        if int(m.group(1)) != 0:
            ip += int(m.group(2))
        else:
            ip += 1
        continue

    m = re.match('jnz (\w+) (-?\d+)', inst)
    if m:
        reg = m.group(1)
        if reg in VARS:
            if VARS[reg] != 0:
                ip += int(m.group(2))
            else:
                ip += 1
        else:
            ip += 1
        continue

    ip += 1

print('value of a: {}'.format(VARS['a']))

