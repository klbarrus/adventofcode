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


VARS = {}
prog = []
ip = 0
numcycles = 20

with open(sys.argv[1]) as f:
    prog = [line.rstrip() for line in f if line.rstrip() != '']
f.close()

done = False
init_a = 1
a_init = init_a
while not done:
    VARS.clear()
    VARS = {'a': init_a}
    a_init = init_a
    ip = 0
    progout = ''

    while ip < len(prog):
        if len(progout) >= numcycles * 2:
            break

        inst = prog[ip]

        # m = re.match('nop', inst)
        # if m:
        #     ip += 1
        #     continue
        #
        # m = re.match('mul (\w+) (\w+) (\w+)', inst)
        # if m:
        #     reg1 = m.group(1)
        #     reg2 = m.group(2)
        #     if reg1 in VARS and reg2 in VARS:
        #         VARS[m.group(3)] = int(VARS[reg1]) * int(VARS[reg2])
        #     ip += 1
        #     continue

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
            reg1_val = convert_to_int(p1) 
            reg2_val = convert_to_int(p2) 
            if reg1_val != 0:
                ip += reg2_val
            else:
                ip += 1
            continue

        m = re.match('out (\w+)', inst)
        if m:
            p1 = m.group(1)
            reg1_val = convert_to_int(p1)
            progout += str(reg1_val)
            ip += 1
            continue

        # m = re.match('tgl (\w+)', inst)
        # if m:
        #     targoff = ip + int(VARS[m.group(1)])
        #     if 0 <= targoff < len(prog):
        #         tglinst = prog[targoff]
        #         m = re.match('(\w+)', tglinst)
        #         if m:
        #             cmd = m.group(1)
        #             newcmd = ''
        #             if cmd == 'inc':
        #                 newcmd = 'dec'
        #             elif cmd == 'dec' or cmd == 'tgl':
        #                 newcmd = 'inc'
        #             elif cmd == 'jnz':
        #                 newcmd = 'cpy'
        #             else:
        #                 newcmd = 'jnz'
        #             prog[targoff] = tglinst.replace(cmd, newcmd)
        #     else:
        #         pass
        #     ip += 1
        #     continue

        ip += 1

    print('initial a = {}, out = {}'.format(init_a, progout))
    if progout == '01' * numcycles:
        done = True
    init_a += 1

print('a: {}'.format(a_init))

