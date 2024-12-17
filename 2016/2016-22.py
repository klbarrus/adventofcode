#!/usr/bin/env python3
# AdventOfCode 2016 Day 22

import sys
import re
from collections import namedtuple


def parse_info(line):
    return [int(x) for x in re.findall('\d+', line)]


def viable_node(na, nb):
    return na.used != 0 and na != nb and na.used <= nb.avail


def get_node(x, y, nl):
    return [nodes for nodes in nl if nodes.x == x and nodes.y == y][0]


def search_maze(s_list, m_dict, xc, yc, steps):
    global max_x, max_y, nodelist, zero_start
    for xd, yd in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x = xc + xd
        y = yc + yd
        if 0 <= x <= max_x and 0 <= y <= max_y:
            nn = get_node(x, y, nodelist)
            if nn not in m_dict and viable_node(nn, zero_start):
                m_dict[nn] = steps + 1
                s_list.append(nn)


Node = namedtuple('Node', 'x y size used avail percent')
nodelist = []
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('/dev'):
            new_node = Node(*parse_info(line))
            nodelist.append(new_node)
f.close()

numv = sum(viable_node(a, b) for a in nodelist for b in nodelist)
print('part 1: {} viable nodes'.format(numv))

max_x = max(node.x for node in nodelist)
max_y = max(node.y for node in nodelist)
data_start = get_node(max_x, 0, nodelist)
print('data starts at {}'.format(data_start))
zero_start = [nodes for nodes in nodelist if nodes.used == 0][0]
print('empty starts at {}'.format(zero_start))

for x in range(0, max_x + 1):
    row = ''
    for y in range(0, max_y + 1):
        node = get_node(x, y, nodelist)
        if x == 0 and y == 0:
            row += 'G'
        elif x == data_start.x and y == data_start.y:
            row += 'D'
        elif x == zero_start.x and y == zero_start.y:
            row += 'Z'
        elif node.percent >= 85:
            row += '#'
        else:
            row += '.'
    print('{}'.format(row))

# find shortest path for empty node to move adjacent (one space above) data
min_steps = 0
adjacent_data = get_node(data_start.x - 1, 0, nodelist)
steps_count = {zero_start: 0}
search = [zero_start]
while search:
    curr = search[0]
    curr_steps = steps_count[curr]
    search = search[1:]
    search_maze(search, steps_count, curr.x, curr.y, curr_steps)
    if adjacent_data in steps_count:
        min_steps = steps_count[adjacent_data]
        break

# steps to move data to adjacent to goal (one space below)
min_steps += 5 * (data_start.x - 1)

# steps for final swap
min_steps += 1

print('part 2: {} steps'.format(min_steps))

