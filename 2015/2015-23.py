#!/usr/bin/env python3
# AdventOfCode 2015 Day 23

import sys

def run_prog(prog, reg):
    ip = 0
    while ip < len(prog):
        curr = prog[ip]
        inst = curr[0]
#        print("{}: {}".format(ip, curr))
        if "hlf" in inst:
            reg[curr[1]] /= 2
        elif "tpl" in inst:
            reg[curr[1]] *= 3
        elif "inc" in inst:
            reg[curr[1]] += 1
        elif "jmp" in inst:
            ip += curr[1] - 1
        elif "jie" in inst:
            if reg[curr[1]] % 2 == 0:
                ip += curr[2] - 1
        elif "jio" in inst:
            if reg[curr[1]] == 1:
                ip += curr[2] - 1
        ip += 1
    #    print("reg {}".format(reg))

prog = []
with open(sys.argv[1])as f:
    for line in f:
        if "hlf" in line or "tpl" in line or "inc" in line:
            inst = line.strip().split() # [op, reg]
        elif "jmp" in line:
            inst = line.strip().split() 
            inst[1] = int(inst[1])      # [jmp, ###]
        elif "jie" in line or "jio" in line:
            inst = line.strip().split()
            inst[1] = inst[1].strip(",")
            inst[2] = int(inst[2])      # [ji?, reg, ###]
        else:
            print("unknown instruction")
        prog.append(inst)
f.close()
#print("{}".format(prog))

reg = {
    'a':0,
    'b':0,
}
run_prog(prog, reg)
print("b is {}".format(reg["b"]))

reg = {
    'a':1,
    'b':0,
}
run_prog(prog, reg)
print("b is {}".format(reg["b"]))
