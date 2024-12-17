#!/usr/bin/env python3
# AdventOfCode 2015 Day 10

import sys

# "112333" -> ["11","2","333"]
def chunk_string(istr):
    oarr = []
    cstr = ""
    prev = istr[0]
    for ch in istr:
        if ch == prev:
            cstr += ch
        else:
            oarr.append(cstr)
            prev = ch
            cstr = str(ch)
    oarr.append(cstr)
    return oarr

# ["11","2","333"] -> "211233"
def flatten_array(iarr):
    ostr = ""
    for x in iarr:
        length = len(x)
        digit = x[0]
        ostr += str(length)
        ostr += str(digit)
    return ostr

orig = sys.argv[1]

out = orig
for i in range(50):
    cs = chunk_string(out)
    out = flatten_array(cs)

#print("result = {}".format(out))
print("length is {}".format(len(out)))