#!/usr/bin/env python3
# AdventOfCode 2016 Day 15

discs_num = [7, 13, 3, 5, 17, 19]
discs_pos = [0,  0, 2, 2,  0,  7]

for part in range(1, 3):
    t = 0
    done = False
    if part == 2:
        discs_num.append(11)
        discs_pos.append(0)
    while not done:
        allpass = True
        for i, (x, y) in enumerate(zip(discs_num, discs_pos)):
            if (t + i + 1 + y) % x != 0:
                allpass = False
        if allpass:
            done = True
        else:
            done = False
            t += 1
    print('part {}: time {}'.format(part, t))

