#!/usr/bin/env python3
# AdventOfCode 2015 Day 11

import sys

def next_str(istr):
    iarr = list(istr)
    cind = -1
    done = False
    while not done:
        rd = iarr[cind]
        if rd != 'z':
            iarr[cind] = chr(ord(rd)+1)
            done = True
        else:
            iarr[cind] = 'a'
# need to carry
            done = False
            cind -= 1
            if cind < -len(istr):
                done = True
                iarr.insert(0,'a')
    ostr = ''.join(iarr)
    return ostr

def search_straight(istr):
    ret = False
    for x in range(len(istr)-2):
        c1 = ord(istr[x])
        c2 = ord(istr[x+1])
        c3 = ord(istr[x+2])
        if c2 == c1+1 and c3 == c2+1:
            ret = True
            break
    return ret

def search_iol(istr):
    ret = False
    for x in istr:
        if x == 'i' or x == 'o' or x == 'l':
            ret = True
            break
    return ret

def search_doubles(istr):
    ret = False
    p1ch = ""
    p2ch = ""
    p1pos = 0
    p2pos = 0
    for x in range(len(istr)-1):
        if istr[x] == istr[x+1]:
            if p1ch == "":
                p1ch = istr[x]
                p1pos = x
            else:
                p2ch = istr[x]
                p2pos = x
        if p1ch != "" and p2ch != "":
            if p1ch != p2ch:
                ret = True
                break   # found 2 different pairs
            elif p2pos != p1pos+1:
                ret = True
                break   # same pair but no overlap
    return ret

password = sys.argv[1]

done = False
while not done:
    b1 = search_iol(password)
    b2 = search_straight(password)
    b3 = search_doubles(password)

    if not b1 and b2 and b3:
        break
    else:
        password = next_str(password)

print("password: {}".format(password))
