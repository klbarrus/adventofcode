#!/usr/bin/env python3
# AdventOfCode 2015 Day 15

import sys

class Ingredients:
    def __init__(self, name, proplist):
        self.name = name
        self.proplist = proplist

    def calc_prop(self, tsp):
        return [x*tsp for x in self.proplist]

    def get_cals(self):
        return self.proplist[-1]

def score_cookie(cm):
    sm = []
    for i in range(len(cm)):
        si = 0
        for j in range(4): # skip calories
            si += cm[j][i]
        sm.append(si)
    score = 1
    for i in range(len(sm)):
        if sm[i] > 0:
            score *= sm[i]
        else:
            score = 0
    return score

def cf_100tsp(tsp):
    if tsp == 100:
        return True
    else: 
        return False

def cf_500cal(cal):
    if cal == 500:
        return True
    else:
        return False

def find_max(cf1, cf2):
    max = 0
    maxlist = []
    for a in range(0, 101):
        for b in range(0, 101):
            for c in range(0, 101):
                for d in range(0, 101):
                    totaltsp = a+b+c+d
                    if cf1:
                        rv = cf1(totaltsp)
                        if not rv:
                            continue
                    pm = [a,b,c,d]
                    if cf2:
                        cals = sum([itm.get_cals() * pm[ind] for ind, itm in enumerate(inglist)])
                        rv = cf2(cals)
                        if not rv:
                            continue
                    cm = [itm.calc_prop(pm[ind]) for ind, itm in enumerate(inglist)]
                    score = score_cookie(cm)
                    if score > max:
                        max = score
                        maxlist = pm
#                   print("ingredient proportions {}".format(pm))
#                   print("calc prop matrix {}".format(cm))
#                   print("ingredient scores {}".format(sm))
#                   print("score {}".format(score))
    return max, maxlist

inglist = []
with open(sys.argv[1]) as f:
    for line in f:
        name, pinfo = line.strip().split(":")
        pnums = [int(x.strip().split()[-1]) for x in pinfo.split(",")]
        ing = Ingredients(name, pnums)
        inglist.append(ing)
f.close()

max, maxlist = find_max(cf_100tsp, None)
print("max score {}".format(max))
print("ingredients {}".format(maxlist))

max, maxlist = find_max(cf_100tsp, cf_500cal)
print("max score {}".format(max))
print("ingredients {}".format(maxlist))
