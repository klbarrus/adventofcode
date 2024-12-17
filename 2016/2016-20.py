#!/usr/bin/env python3
# AdventOfCode 2016 Day 20

import sys


# read in firewall rules
rules = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if len(line) > 0:
            lo, hi = line.split('-')
            lo = int(lo)
            hi = int(hi)
            rules.append((lo, hi))
f.close()

rules.sort()
print('{} firewall rules'.format(len(rules)))

# coalesce firewall rules
new_rules = []
while rules: 
    curr_lo = rules[0][0]
    curr_hi = rules[0][1]
    j = 1
    # look for overlap with first rule 
    while j < len(rules):
        next_lo = rules[j][0]
        next_hi = rules[j][1]
        if next_hi + 1 < curr_lo:   # next range entirely below
            break
        elif curr_hi + 1 < next_lo: # next range entirely above
            break
        else:
            curr_lo = min(curr_lo, next_lo)
            curr_hi = max(curr_hi, next_hi)
        j += 1
    new_rules.append((curr_lo, curr_hi))
    del rules[0:j]

print('{} firewall rules after coalescing'.format(len(new_rules)))
print('')
print('part 1: first address not blocked is {}'.format(new_rules[0][1] + 1))

total = 0
for i in range(1, len(new_rules)):
    total += new_rules[i][0] - new_rules[i-1][1] - 1
# add addresses between top of firewall rules and max ipaddr
total += (2**32 - 1) - new_rules[-1][1]

print('part 2: {} total addresses not blocked'.format(total))

