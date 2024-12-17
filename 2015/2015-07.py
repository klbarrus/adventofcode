#!/usr/bin/env python3
# AdventOfCode Day 07

# this is very ugly, could use an overhaul
# for part 2, edit the input file to reassign b then rerun

import sys
import re

# assignment of number to variable
rasn = re.compile(r'(\d+) -> ([a-z]\w*)')
rasv = re.compile(r'([a-z]\w+) -> ([a-z]\w*)')
# NOT operator
rnot = re.compile(r'[A-Z]+ ([a-z]\w*) -> ([a-z]\w*)')

# all the other operators, can take variables and/or number
rops = re.compile(r'(\w*) ([A-Z]+) (\w*) -> ([a-z]\w*)')

sym = {}
inst = []
with open(sys.argv[1]) as f:
    for line in f:
# split instructions into tokens

        if "AND" in line or "OR" in line or "SHIFT" in line:
            m = rops.search(line)
            toks = []
            toks.append(m.group(2)) # op
            toks.append(m.group(4)) # dest
            toks.append(m.group(1)) # src1
            toks.append(m.group(3)) # src2
            inst.append(toks)
            continue

        if "NOT" in line:
            m = rnot.search(line)
            toks = []
            toks.append("NOT")      # op
            toks.append(m.group(2)) # dest
            toks.append(m.group(1)) # src
            inst.append(toks)
            continue

        m = rasn.search(line)
        if m:
# assignment of number to dest var can be done immediately
# update symbol table
            sym[m.group(2)] = int(m.group(1))
            continue   

        m = rasv.search(line)
        if m:
            toks = []
            toks.append("RASV")     # op
            toks.append(m.group(2)) # dest
            toks.append(m.group(1)) # src
            inst.append(toks) 
            continue  

        print("????: {}".format(line))
f.close()

# initial symbols
#for k,v in sym.items():
#    print("{} = {}".format(k,v))

# loop over instructions
#   process ones that have inputs ready, don't append
#   appends ones that aren't ready
# update inst list and repeat until no more instructions

#print("starting - {} instructions".format(len(inst)))

done = False
iprev = len(inst)
while not done:
    newinst = []
    for i in inst:
        if i[0] == "AND":
            intarg = False
            try:
                i2 = int(i[2])
                intarg = True
            except ValueError:
                intarg = False

            if intarg:
                if i[3] in sym:
                    #print("{} = {} {} {}".format(i[1],i[2],i[0],i[3]))
                    sym[str(i[1])] = int(i[2]) & int(sym[i[3]])
                else:
                    newinst.append(i)
            else:
                if i[2] in sym and i[3] in sym:
                    #print("{} = {} {} {}".format(i[1],i[2],i[0],i[3]))
                    sym[str(i[1])] = int(sym[i[2]]) & int(sym[i[3]])
                else:
                    newinst.append(i)
        elif i[0] == "OR":
            if i[2] in sym and i[3] in sym:
                #print("{} = {} {} {}".format(i[1],i[2],i[0],i[3]))
                sym[str(i[1])] = int(sym[i[2]]) | int(sym[i[3]])
            else:
                newinst.append(i)
        elif i[0] == "LSHIFT":  
            if i[2] in sym:
                #print("{} = {} {} {}".format(i[1],i[2],i[0],i[3]))
                res = sym[i[2]] << int(i[3])
                sym[str(i[1])] = res
            else:
                newinst.append(i)
        elif i[0] == "RSHIFT":  
            if i[2] in sym:
                #print("{} = {} {} {}".format(i[1],i[2],i[0],i[3]))
                res = sym[i[2]] >> int(i[3])
                sym[str(i[1])] = res
            else:
                newinst.append(i)
        elif i[0] == "NOT":
            if i[2] in sym:
                #print("{} = {} {}".format(i[1],i[0],i[2]))
                sym[str(i[1])] = ~ int(sym[i[2]])
            else:
                newinst.append(i)
        elif i[0] == "RASV":            
            if i[2] in sym:
                #print("{} = {}".format(i[2],i[1]))
                sym[str(i[1])] = int(sym[i[2]])
            else:
                newinst.append(i)

    if "a" in sym:
        print("value of a: {}".format(sym["a"]))
        done = True
        break

#    inow = len(newinst)
#    if inow == iprev:
#        done = True
#        break

#    iprev = inow

#    if len(newinst) == 0:
#        done = True
#    else:
#        print("{} instructions left".format(len(newinst)))
#        inst = []
    inst = newinst

#print("symbols")
# final symbols
#for k,v in sym.items():
#    print("{} = {}".format(k,v))

#print("instructions")
#for i in inst:
#    print(i)