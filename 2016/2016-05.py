#!/usr/bin/env python3
# AdventOfCode 2016 Day 05

import hashlib

door_id = 'wtnhxymk'
N = 5
PWD_LEN = 8
pwd_1 = ''
pwd_2 = ''
pwd_2_d = {}
index = 0
done1 = False
done2 = False

while not (done1 and done2):
    combo = door_id + str(index)
    m = hashlib.md5()
    m.update(combo.encode('utf-8'))
    dig = m.hexdigest()
    lead = str(dig)[0:N]
    if lead == '0'*N:
        if not done1:
            ch = str(dig)[N]
            pwd_1 += ch
            if len(pwd_1) == PWD_LEN:
                done1 = True
        if not done2:
            pos = int(str(dig)[N], 16)
            if pos < PWD_LEN:
                ch = str(dig)[N+1]
                if pos not in pwd_2_d:
                    pwd_2_d[pos] = ch
                if len(pwd_2_d) == PWD_LEN:
                    done2 = True
    index += 1

print('password 1: {}'.format(pwd_1))

for k in sorted(pwd_2_d):
    pwd_2 += pwd_2_d[k]
print('password 2: {}'.format(pwd_2))

