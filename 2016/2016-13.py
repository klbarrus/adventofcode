#!/usr/bin/env python3
# AdventOfCode 2016 Day 13

PUZZ = 1350
# PUZZ = 10
OPEN = 0
WALL = 1
START_X = 1
START_Y = 1
END_X = 31
END_Y = 39
# END_X = 7
# END_Y = 4
maze = {}


def maze_coord(x, y):
    fxy = (x + y) ** 2 + 3 * x + y + PUZZ
    bits = bin(fxy).count("1")
    if bits % 2 == 0:
        rv = OPEN
    else:
        rv = WALL
    return rv


def search_maze(s_list, m_dict, xc, yc, steps):
    if xc < 0 or yc < 0:
        return
    if maze_coord(xc, yc) == WALL:
        return
    if (xc, yc) in m_dict:
        return
    m_dict[(xc, yc)] = steps
    s_list.append((xc, yc))


# for i in range(0, 10):
#     row = ''
#     for j in range(0, 10):
#         if maze_coord(i, j) == OPEN:
#             row += '.'
#         else:
#             row += '#'
#     print('{}'.format(row))

search = [(START_X, START_Y)]
maze = {(START_X, START_Y): 0}
while search:
    (x, y) = search[0]
    curr_steps = maze[(x, y)]
    search = search[1:]
    search_maze(search, maze, x - 1, y, curr_steps + 1)
    search_maze(search, maze, x + 1, y, curr_steps + 1)
    search_maze(search, maze, x, y - 1, curr_steps + 1)
    search_maze(search, maze, x, y + 1, curr_steps + 1)
    if (END_X, END_Y) in maze:
        print('{} steps to ({},{})'.format(maze[(END_X, END_Y)], END_X, END_Y))
        break

num = 0
for loc in maze:
    if maze[loc] <= 50:
        num += 1
print('{} reachable in 50 steps'.format(num))

