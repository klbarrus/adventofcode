#!/usr/bin/env python3
# AdventOfCode 2016 Day 01

import sys

compass = "NESW"
point = 0           # index of current compass direction
bx = 0
by = 0
visit = {(0,0): 1}
first = None

def update_visit(v, tx, ty):
    global first
#    print('visiting ({},{})'.format(tx,ty))
    if (tx,ty) in v:
        if first == None:
            first = (tx,ty)
    else:
        v[(tx,ty)] = 1

with (open(sys.argv[1])) as f:
    data = f.readlines()
    for line in data:
        vel = line.split(' ')
        # print('{}'.format(vel))
        for dn in vel:
            dn = dn[:-1]        # truncate last char (,)
            # print('{}'.format(dn))
            # update what direction we're facing
            if dn[0] == 'R':
                point = point + 1
            else:
                point = point - 1
            point = point % 4
            # print('now facing {}'.format(compass[point]))

            # walk blocks
            blocks = int(dn[1:])
            # print('walk {} blocks'.format(blocks))
            if point == 0:      # facing north
                for i in range(by+1,by+blocks+1):
                    update_visit(visit,bx,i)
                by += blocks
            elif point == 1:    # facing east
                for i in range(bx+1, bx+blocks+1):
                    update_visit(visit, i, by)
                bx += blocks
            elif point == 2:    # facing south
                for i in range(by-1,by-blocks-1,-1):
                    update_visit(visit,bx,i)
                by -= blocks
            else:               # facing west
                for i in range(bx-1, bx-blocks-1,-1):
                    update_visit(visit, i, by)
                bx -= blocks
            # print('stop at ({},{})'.format(bx, by))
            # print('')
f.close()

print('end at ({},{})'.format(bx, by))
print('{} blocks away'.format(abs(bx)+abs(by)))
print('')
if first != None:
    print('first block visited twice: {}'.format(first))
    print('{} blocks away'.format(abs(first[0])+abs(first[1])))
else:
    print('no block visited twice')
