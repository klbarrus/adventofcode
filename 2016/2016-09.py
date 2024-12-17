#!/usr/bin/env python3
# AdventOfCode 2016 09

import sys
import re


mark = r'(\(\d+x\d+\))'
mark_det = r'\((\d+)x(\d+)\)'


def decomp_count(list, nested):
    rv = 0
    i = 0
    maxidx = len(list)
    while i < maxidx:
        chunk = list[i]
        if len(chunk) > 0:
            mark_info = re.split(mark_det, chunk)
            if len(mark_info) > 1:
                num = int(mark_info[1])
                rep = int(mark_info[2])
                sublist = []
                charcount = 0
                while charcount < num:
                    i += 1
                    charcount += len(list[i])
                    sublist.append(list[i])
                if nested:
                    rv += rep * decomp_count(sublist, nested)
                else:
                    tlen = 0
                    for tc in sublist:
                        tlen += len(tc)
                    rv += rep * tlen
                i += 1
            else:
                rv += len(chunk)
                i += 1
        else:
            i += 1
    return rv


with open(sys.argv[1]) as f:
    data = f.read().replace('\n', '')
f.close()
data_list = re.split(mark, data)

lenout = decomp_count(data_list, False)
print('format 1 length: {}'.format(lenout))

lenout = decomp_count(data_list, True)
print('format 2 length: {}'.format(lenout))

