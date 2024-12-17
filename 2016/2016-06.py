#!/usr/bin/env python3
# AdventOfCode 2016 Day 06

import sys

letters = {}
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        i = 0
        for ch in line:
            if i not in letters:
                letters[i] = {}
                letters[i][ch] = 1
            else:
                sd = letters[i]
                if ch in sd:
                    sd[ch] += 1
                else:
                    sd[ch] = 1
            i += 1
f.close()

msg_1 = ''
msg_2 = ''
for k in sorted(letters):
    sd = letters[k]
    ch = max(sd.keys(), key=(lambda x: sd[x]))
    msg_1 += ch
    ch = min(sd.keys(), key=(lambda x: sd[x]))
    msg_2 += ch
print('message 1: {}'.format(msg_1))
print('message 2: {}'.format(msg_2))

