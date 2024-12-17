#!/usr/bin/env python3
# AdventOfCode 2016 Day 10

import sys
import re

bots = {}
out = {}
VAL1 = 61
VAL2 = 17


def add_val_bot(val, bot):
    if bot in bots:
        oldbot = bots[bot]
        if 'val1' in oldbot:
            oldbot['val2'] = val
        else:
            oldbot['val1'] = val
    else:
        newbot = {'val1': val}
        bots[bot] = newbot


def add_outputs(bot, lo, lonum, hi, hinum):
    if bot in bots:
        genbot = bots[bot]
    else:
        genbot = {}
        bots[bot] = genbot
    genbot['lo'] = lo + ' ' + lonum
    genbot['hi'] = hi + ' ' + hinum


def update_bot(bot):
    currbot = bots[bot]
    v1 = int(currbot['val1'])
    v2 = int(currbot['val2'])
    hi = max(v1, v2)
    lo = min(v1, v2)
    if hi == VAL1 and lo == VAL2:
        print('bot {} comparing value-{} and value-{}'.format(bot, VAL1, VAL2))
    m = re.match('output (\d+)', bots[bot]['lo'])
    if m:
        out[m.group(1)] = lo
    m = re.match('bot (\d+)', bots[bot]['lo'])
    if m:
        add_val_bot(lo, m.group(1))
    m = re.match('output (\d+)', bots[bot]['hi'])
    if m:
        out[m.group(1)] = hi
    m = re.match('bot (\d+)', bots[bot]['hi'])
    if m:
        add_val_bot(hi, m.group(1))
    del bots[bot]['val1']
    del bots[bot]['val2']


with open(sys.argv[1]) as f:
    for line in f:
        m = re.match('value (\d+) .* (\d+)', line)
        if m:
            add_val_bot(m.group(1), m.group(2))
        m = re.match('bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)', line)
        if m:
            add_outputs(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5))
f.close()

done = False
while not done:
    for botnum, inst in bots.items():
        if 'val1' in inst and 'val2' in inst:
            update_bot(botnum)
    if '0' in out and '1' in out and '2' in out:
        out0 = int(out['0'])
        out1 = int(out['1'])
        out2 = int(out['2'])
        print('product is {}'.format(out0 * out1 * out2))
        done = True

