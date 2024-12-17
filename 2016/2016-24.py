#!/usr/bin/env python3
# AdventOfCode 2016 Day 24

import sys
import itertools

maze = []
poi = {}


def pairwise(it):
    a, b = iter(it)
    next(b, None)
    return zip(a, b)


def search_maze(s_list, m_dict, xc, yc, steps):
    if 0 <= xc < len(maze) and 0 <= yc < len(maze[xc]):
        if maze[xc][yc] != '#' and (xc, yc) not in m_dict:
            m_dict[(xc, yc)] = steps
            s_list.append((xc, yc))


# read in maze
with open(sys.argv[1]) as f:
    for line in f:
        maze.append(line.rstrip())
f.close()

# get coords for POIs
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] != '.' and maze[i][j] != '#':
            poi[maze[i][j]] = (i, j)

# find shortest path between each pair of POIs
min_steps = {}
for (p1, p2) in itertools.combinations(poi.keys(), 2):
    steps_count = {poi[p1]: 0}
    search = [poi[p1]]
    maze_end = poi[p2]
    while search:
        (x, y) = search[0]
        curr_steps = steps_count[(x, y)]
        search = search[1:]
        search_maze(search, steps_count, x - 1, y, curr_steps + 1)
        search_maze(search, steps_count, x + 1, y, curr_steps + 1)
        search_maze(search, steps_count, x, y - 1, curr_steps + 1)
        search_maze(search, steps_count, x, y + 1, curr_steps + 1)
        if maze_end in steps_count:
            min_steps[(p1, p2)] = curr_steps + 1
            min_steps[(p2, p1)] = curr_steps + 1
            break
for a in poi.keys():
    min_steps[(a, a)] = 0

for part in [1, 2]:
    overall_min_steps = sum(min_steps[(a, b)] for a in poi.keys() for b in poi.keys())
    overall_min_path = [] 
    # enumerate all paths
    for path in itertools.permutations(poi.keys(), len(poi)):
        if path[0] != '0':
            continue
        p1 = path[0]
        dist = 0
        for i in range(1, len(path)):
            p2 = path[i]
            dist += min_steps[(p1, p2)]
            p1 = p2
        if part == 2:
            dist += min_steps[(path[-1], '0')]
        if dist < overall_min_steps:
            overall_min_steps = dist
            overall_min_path = list(path)
            if part == 2:
                overall_min_path.append('0')

    print('part {}: min {} steps using path {}'.format(part, overall_min_steps, overall_min_path))

