#!/usr/bin/env python3
# AdventOfCode 2016 Day 23 

import sys
import re


def convert_to_int(val):
    rv = 0
    try:
        rv = int(val)
    except ValueError as verr:
        if val in VARS:
            rv = VARS[val]
    return rv


# VARS = {'a': 7}
VARS = {'a': 12}
prog = []
ip = 0

with open(sys.argv[1]) as f:
    for line in f:
        ls = line.rstrip()
        if ls:
            prog.append(ls)
f.close()

# optimize assembunny instructions into a multiply instruction
prog[2] = 'nop'
prog[3] = 'nop'
prog[4] = 'nop'
prog[5] = 'nop'
prog[6] = 'nop'
prog[7] = 'nop'
prog[8] = 'nop'
prog[9] = 'mul b a a'

while ip < len(prog):
    inst = prog[ip]

    m = re.match('nop', inst)
    if m:
        ip += 1
        continue

    m = re.match('mul (\w+) (\w+) (\w+)', inst)
    if m:
        reg1 = m.group(1)
        reg2 = m.group(2)
        if reg1 in VARS and reg2 in VARS:
            VARS[m.group(3)] = int(VARS[reg1]) * int(VARS[reg2])
        ip += 1
        continue

    m = re.match('cpy (-?\w+) (\w+)', inst)
    if m:
        VARS[m.group(2)] = convert_to_int(m.group(1))
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

    m = re.match('jnz (-?\w+) (-?\w+)', inst)
    if m:
        p1 = m.group(1)
        p2 = m.group(2)
        reg1_val = 0
        reg2_val = 0
        try:
            reg1_val = int(p1)
        except ValueError as verr:
            if p1 in VARS:
                reg1_val = VARS[p1]
        try:
            reg2_val = int(p2)
        except ValueError as verr:
            if p2 in VARS:
                reg2_val = VARS[p2]
        if reg1_val != 0:
            ip += reg2_val
        else:
            ip += 1
        continue

    m = re.match('tgl (\w+)', inst)
    if m:
        targoff = ip + int(VARS[m.group(1)])
        if 0 <= targoff < len(prog):
            tglinst = prog[targoff]
            m = re.match('(\w+)', tglinst)
            if m:
                cmd = m.group(1)
                newcmd = ''
                if cmd == 'inc':
                    newcmd = 'dec'
                elif cmd == 'dec' or cmd == 'tgl':
                    newcmd = 'inc'
                elif cmd == 'jnz':
                    newcmd = 'cpy'
                else:
                    newcmd = 'jnz'
                prog[targoff] = tglinst.replace(cmd, newcmd)
        else:
            pass
        ip += 1
        continue

    ip += 1

print('value of a: {}'.format(VARS['a']))

