#!/usr/bin/env python3
# AdventOfCode 2015 Day 21

import itertools
import copy

WEAPONS = [
    ["Dagger", 8, 4, 0],
    ["Shortwword", 10, 5, 0],
    ["Warhammer", 25, 6, 0],
    ["Longsword", 40, 7, 0],
    ["Greataxe", 74, 8, 0],
]

ARMOR = [
    ["None", 0, 0, 0],
    ["Leather", 13, 0, 1],
    ["Chainmail", 31, 0, 2],
    ["Splintmail", 53, 0, 3],
    ["Bandedmail", 75, 0, 4],
    ["PLatemail", 102, 0, 5],
]

RINGS = [
    ["None", 0, 0, 0],
    ["Damage +1", 25, 1, 0],
    ["Damage +2", 50, 2, 0],
    ["Damage +3", 100, 3, 0],
    ["Defense +1", 20, 0, 1],
    ["Defense +2", 40, 0, 2],
    ["Defense +3", 80, 0, 3],
]

BOSS = {
    'hp':109,
    'damage':8,
    'armor':2,
}

PLAYER = {
    'hp':100,
    'damage':0,
    'armor':0,
}

def goldspent(w, a, r):
    gs = w[1]
    gs += a[1]
    gs += r[0][1] + r[1][1]
    return gs

def combat(w, a, r):
    gold = goldspent(w, a, r)
    boss = copy.copy(BOSS)
    player = copy.copy(PLAYER)
    player['damage'] = w[2] + r[0][2] + r[1][2]
    player['armor'] = a[3] + r[0][3] + r[1][3]
    while player['hp'] > 0 and boss['hp'] > 0:
        dam = player['damage'] - boss['armor']
        if dam < 1:
            dam = 1
        boss['hp'] -= dam
        if boss['hp'] <= 0:
            pwin = True
            break
        dam = boss['damage'] - player['armor']
        if dam < 1:
            dam = 1
        player['hp'] -= dam
        if player['hp'] <= 0:
            pwin = False
            break
#    print("player win {}, gold {}".format(pwin, gold))
    return pwin, gold

minwin = 1000
maxlose = 0
for w in WEAPONS:
    for a in ARMOR:
# handle case of no rings
        pwin, gold = combat(w, a, (RINGS[0], RINGS[0]))
        if pwin:
            if gold < minwin:
                minwin = gold 
        else:
            if gold > maxlose:
                maxlose = gold     
# handle rest of gear combinations          
        for r in itertools.combinations(RINGS, 2):
            pwin, gold = combat(w, a, r)
            if pwin:
                if gold < minwin:
                    minwin = gold
            else:
                if gold > maxlose:
                    maxlose = gold     
print("cheapest win is {} gold".format(minwin))
print("priciest loss is {} gold".format(maxlose))
