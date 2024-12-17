#!/usr/bin/env python3
# AdventOfCode 2015 Day 22

import copy

SPELLS = {
    'Magic Missile' : 53,
    'Drain' : 73,
    'Shield' : 113,
    'Poison' : 173,
    'Recharge' : 229,
}

INIT_GAME_STATE = {
    'Spells': [],
    'PMana' : 500,
    'PHit' : 50,
    'BHit' : 58,        # my puzzle input
    'BDam' : 9,         # my puzzle input
    'Shield' : 0,
    'Poison' : 0,
    'Recharge' : 0,
    'ManaUsed' : 0,
}

def playerArmor(gs):
    if gs['Shield'] > 0:
        return 7
    else:
        return 0

def playerWin(gs):
    if gs['PHit'] > 0 and gs['PMana'] >= 0 and gs['BHit'] <= 0:
        return True
    return False

def printStats(gs):
    armor = playerArmor(gs)
    print("- Player has {} hit points, {} armor, {} mana".format(gs['PHit'], armor, gs['PMana']))
    print("- Boss has {} hit points".format(gs['BHit']))

def applyEffects(gs):
    if gs['Poison'] > 0:
        gs['Poison'] -= 1
        gs['BHit'] -= 3

    if gs['Recharge'] > 0:
        gs['Recharge'] -= 1
        gs['PMana'] += 101        
    
    if gs['Shield'] > 0:
        gs['Shield'] -= 1

def resolveCombatPlayer(sp, gs, part2):
#    print("-- Player turn --")
#    printStats(gs)
#    print("Player casts {}".format(sp))
    if part2:
        gs['PHit'] -= 1
    applyEffects(gs)
# player casts a spell
    if sp == 'Drain':
        gs['PHit'] += 2
        gs['BHit'] -= 2
    elif sp == 'Magic Missile':
        gs['BHit'] -= 4
    elif sp == 'Poison':
        gs['Poison'] = 6
    elif sp == 'Recharge':
        gs['Recharge'] = 5
    elif sp == 'Shield':
        gs['Shield'] = 6
    gs['PMana'] -= SPELLS[sp]
    gs['ManaUsed'] += SPELLS[sp]

def resolveCombatBoss(gs):
#    print("-- Boss turn --")
#    printStats(gs)
    applyEffects(gs)
# boss attacks    
    dam = max(gs['BDam'] - playerArmor(gs), 1)
    gs['PHit'] -= dam
#    print("Boss attacks for {} damage".format(dam))

# keep going until player or boss is dead, or player is out of mana
def endCondition(gs):
    if gs['PHit'] <= 0 or gs['PMana'] < 0 or gs['BHit'] <= 0:
        return True
    return False

minmana = 999999
mings = []

def checkEndCondition(gs):
    global minmana
    global mings
    if endCondition(gs):
        if playerWin(gs):
            if gs['ManaUsed'] < minmana:
                minmana = gs['ManaUsed']
                mings = gs
                print("win with {} mana".format(minmana))
        return True
    return False

def doCombat(sp, gs, part2):
    gs['Spells'].append(sp)
    resolveCombatPlayer(sp, gs, part2)
    if checkEndCondition(gs):
        return
    resolveCombatBoss(gs)
    if checkEndCondition(gs):
        return
# no need to continue searching along this path if we're already using 
# more mana than a previously found win
    if gs['ManaUsed'] > minmana:
        return
    castable = ['Drain', 'Magic Missile']
# spells with a remaining duration of 1 or less can be recast
# (spells can be cast in the same turn they expire)
    if gs['Poison'] <= 1:
        castable.append('Poison')
    if gs['Recharge'] <= 1:
        castable.append('Recharge')
    if gs['Shield'] <= 1:
        castable.append('Shield')     
    for i in castable:
        up = copy.deepcopy(gs)
        doCombat(i, up, part2)

spells = sorted(SPELLS.keys())
gs = INIT_GAME_STATE
for sp in spells:
    up = copy.deepcopy(gs)
    doCombat(sp, up, False)

print("min mana for player win: {}".format(minmana))
print("min mana winning game:")
print("{}".format(mings))
print("")

minmana = 99999
gs = INIT_GAME_STATE
for sp in spells:
    up = copy.deepcopy(gs)
    doCombat(sp, up, True)

print("min mana for player win in part 2: {}".format(minmana))
print("min mana winning game in part 2:")
print("{}".format(mings))
