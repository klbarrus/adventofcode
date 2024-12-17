#!/usr/bin/env python3
# AdventOfCode 2016 Day 17


import hashlib
from collections import namedtuple
import copy

PASSCODE = 'ioramepc'
#PASSCODE = 'hijkl'
#PASSCODE = 'ihgpwlah'
#PASSCODE = 'kglvqrro'
#PASSCODE = 'ulqzkmiv'

Coord = namedtuple('Coord', 'x y')
start_room = Coord(0, 3)
end_room = Coord(3, 0)

VAULT = {
        'path': '',
        'pos': start_room,
        'steps': 0,
        }

COMPASS = {
        'U': Coord(0, 1),
        'D': Coord(0, -1),
        'L': Coord(-1, 0),
        'R': Coord(1, 0)
        }


def get_path_hash(p):
    m = hashlib.md5()
    m.update(p.encode('utf-8'))
    dig = m.hexdigest()
    return dig[0:4]


def move_from(r):
    rv = []
    curr_path = PASSCODE + r['path']
    doors = get_path_hash(curr_path)
    legal_moves = ''
    if 'b' <= doors[0] <= 'f' and r['pos'].y < 3:
        legal_moves += 'U'
    if 'b' <= doors[1] <= 'f' and r['pos'].y > 0:
        legal_moves += 'D'
    if 'b' <= doors[2] <= 'f' and r['pos'].x > 0:
        legal_moves += 'L'
    if 'b' <= doors[3] <= 'f' and r['pos'].x < 3:
        legal_moves += 'R'
    for dd in legal_moves:
        next_room = copy.deepcopy(VAULT)
        next_room['path'] = r['path'] + dd
        next_room['steps'] = r['steps'] + 1
        next_room['pos'] = Coord(r['pos'].x + COMPASS[dd].x, r['pos'].y + COMPASS[dd].y)
        rv.append(next_room)
    return rv


def check_win_1(rooms):
    rv = False
    for r in rooms:
        if r['pos'] == end_room:
            rv = True
            print('{} {}'.format(r['path'], r['steps']))
    return rv


def check_win_2(rooms):
    global max_steps
    rv = []
    for r in rooms:
        if r['pos'] == end_room:
            if r['steps'] > max_steps:
                max_steps = r['steps']
        else:
            rv.append(r)    # filter out paths that visit the end room
    return rv


part2 = True
max_steps = 0

curr_rooms = [VAULT]
done = False
while not done:
    all_moves = []
    for room in curr_rooms:
        next_rooms = move_from(room)
        all_moves += next_rooms
    if not len(all_moves):  # paths lead to room with no exits
        done = True
        print('dead end')
    else:
        if not part2:
            done = check_win_1(all_moves)
        else:
            all_moves = check_win_2(all_moves)
    curr_rooms = all_moves

if part2:
    print('max steps {}'.format(max_steps))

