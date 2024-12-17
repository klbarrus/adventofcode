#!/usr/bin/env python3
# AdventOfCode 2015 Day 14

import sys

class Reindeer:
    def __init__(self, name, speed, duration, rest):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest = rest

# calc how far a reindeer flies for a given time
    def dist(self, time):
        cycle = self.duration + self.rest
        num, rem = divmod(time, cycle)
        dist = num * self.speed * self.duration
        if rem < self.duration:
            dist += rem * self.speed
        else:
            dist += self.speed * self.duration
        return dist

rl = []
ticks = 2503
with open(sys.argv[1]) as f:
    for line in f:
        info = line.split()
        name = info[0]
        speed = int(info[3])
        duration = int(info[6])
        rest = int(info[-2])
        r = Reindeer(name, speed, duration, rest)
        rl.append(r)
f.close()

maxdist = 0
for r in rl:
    dist = r.dist(ticks)
    if dist > maxdist:
        maxdist = dist
        winner = r.name

print("winner is {}, flying {} km".format(winner, maxdist))

for r in rl:
    r.points = 0

for time in range(1, ticks+1):
    dists = [r.dist(time) for r in rl]
    maxdist = max(dists)
# at tick time, first place is maxdist, so check if any reindeer match it
    for i, r in enumerate(rl):
        if dists[i] == maxdist:
            r.points += 1

maxpoints = 0
for r in rl:
    if r.points > maxpoints:
        maxpoints = r.points
        winner = r.name

print("point winner is {} with {} points".format(winner, maxpoints))
