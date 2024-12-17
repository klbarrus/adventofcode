#!/usr/bin/env python3
# AdventOfCode 2015 Day 04

import hashlib
key = "ckczppom"
done = False
trail = 0
N = 6 # leading 0's to look for
while not done:
    coin = key + str(trail)
    m = hashlib.md5()
    m.update(coin.encode('utf-8'))
    dig = m.hexdigest()
    lead = str(dig)[0:N]
#    print("digest is {}".format(dig))
#    print("lead chars: {}".format(lead))
    if lead == "0"*N:
        done = True
    else:
        trail += 1
    
print("Number: {}".format(trail))
