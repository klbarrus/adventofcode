#!/usr/bin/env python3
# AdventOfCode 2016 Day 14

import hashlib
import re

SALT = 'ahsbgdzn'
# SALT = 'abc'
KEY = 64
NEXT_KEYS = 1000
STRETCH = 2017


def get_hash(h_list,n, part2):
    if n < len(h_list):
        return h_list[n]
    else:
        data = SALT + str(n)
        if part2:
            numiter = STRETCH
        else:
            numiter = 1
        for i in range(0, numiter):
            m = hashlib.md5()
            m.update(data.encode('utf-8'))
            dig = m.hexdigest()
            data = dig
        h_list.append(dig)
        return dig


def is_key(h_list, n, part2):
    rv = False
    h = get_hash(h_list, n, part2)
    m = re.search(r'(\w)\1\1', h)
    if m:
        ch = m.group(1)
        for i in range(n + 1, n + NEXT_KEYS + 1):
            he = get_hash(h_list, i, part2)
            m = re.search(ch * 5, he)
            if m:
                # print('key found')
                # print('  {} in {}, index {}'.format(ch * 3, h, n))
                # print('  {} in {}, index {}'.format(ch * 5, he, i))
                rv = True
    return rv


for i in range(0, 2):
  index = 0
  keys = []
  hashes = []
  done = False
  while not done:
      if i == 0:
          part2 = False
      else:
          part2 = True
      if is_key(hashes, index, part2):
          keys.append(index)
          if len(keys) == KEY:
              done = True
      index += 1
  print('Part {}: key {} at index {}'.format(i + 1, KEY, keys[KEY - 1]))

