#!/usr/bin/env python3
# AdventOfCode 2016 Day 02

import sys

KEYPAD1 = [['1', '2', '3'],
           ['4', '5', '6'],
           ['7', '8', '9']]
code1 = ""

sr = 1  # start part 1 on '5' - row 1 col 1
sc = 1

with (open(sys.argv[1])) as f:
    for line in f:
        line = line.rstrip()
        if len(line) == 0:
            break
        for ch in line:
            if ch == 'L':
                r = 0
                c = -1
            elif ch == 'R':
                r = 0
                c = 1
            elif ch == 'U':
                r = -1
                c = 0
            elif ch == 'D':
                r = 1
                c = 0
            else:
                break

            srn = sr + r
            scn = sc + c
            srn = max(0, srn)
            srn = min(2, srn)
            scn = max(0, scn)
            scn = min(2, scn)

#            print('{} - start {}, end {}'.format(ch, KEYPAD1[sr][sc], KEYPAD1[srn][scn]))
            sr = srn
            sc = scn

#        print('{}'.format(KEYPAD1[sr][sc]))
        code1 += KEYPAD1[sr][sc]
    print('code 1: {}'.format(code1))
f.close()

KEYPAD2 = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', '1', ' ', ' ', ' '],
           [' ', ' ', '2', '3', '4', ' ', ' '],
           [' ', '5', '6', '7', '8', '9', ' '],
           [' ', ' ', 'A', 'B', 'C', ' ', ' '],
           [' ', ' ', ' ', 'D', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
code2 = ""

sr = 3  # start at '5', which is row 3 col 1
sc = 1

with (open(sys.argv[1]))as f:
    for line in f:
        line = line.rstrip()
        if len(line) == 0:
            break
        for ch in line:
            if ch == 'L':
                r = 0
                c = -1
            elif ch == 'R':
                r = 0
                c = 1
            elif ch == 'U':
                r = -1
                c = 0
            elif ch == 'D':
                r = 1
                c = 0
            else:
                break

            srn = sr + r
            scn = sc + c
            if KEYPAD2[srn][scn] == ' ':
                srn = sr
                scn = sc

#            print('{} - start {}, end {}'.format(ch, KEYPAD2[sr][sc], KEYPAD2[srn][scn]))
            sr = srn
            sc = scn

#        print('{}'.format(KEYPAD2[sr][sc]))
        code2 += KEYPAD2[sr][sc]
    print('code 2: {}'.format(code2))
f.close()
