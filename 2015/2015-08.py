#!/usr/bin/env python3
# AdventOfCode Day 08

import sys

numstr = 0
nummem = 0
numenc = 0
with open(sys.argv[1]) as f:
    for line in f:
        # get rid of trailing \n
        line = line.rstrip()
        # get rid of leading and trailing quotes but count those string chars
        line = line[1:-1]
        numstr += 2 # 2 chars for the quotes
        numenc += 6 # 6 chars for encoded quotes

        lar = list(line)
        i = 0
        while i < len(lar):
            if lar[i] == '\\':      # escape char
                if lar[i+1] == '"': # \" sequence found
                    numstr += 2
                    nummem += 1
                    numenc += 4
                    i += 2
                elif lar[i+1] == '\\':  # \\ sequence found
                    numstr += 2
                    nummem += 1
                    numenc += 4
                    i += 2
                elif lar[i+1] == 'x':   # \xcc sequence found
                    numstr += 4
                    nummem += 1
                    numenc += 5
                    i += 4
                else:
                    print("unknown escape sequence \\{}".format(lar[i+1]))
                    i += 1
            else:
                # regular char
                numstr += 1
                nummem += 1
                numenc += 1
                i += 1
f.close()
print("string chars {} - mem chars {} = {}".format(numstr,nummem, numstr-nummem))
print("encoded chars {} - string chars {} = {}".format(numenc,numstr,numenc-numstr))