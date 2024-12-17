#!/usr/bin/env python3
# AdventOfCode 2016 Day 04

import sys
import re


def count_letters(enc):
	rv = {}
	for ch in enc:
		if ch == '-':
			continue
		if ch in rv:
			rv[ch] += 1
		else:
			rv[ch] = 1
	return rv


def make_checksum(lc):
	rv = ''
	inv_dict = {}
	for k, v in lc.items():
		inv_dict[v] = inv_dict.get(v, [])
		inv_dict[v].append(k)
	k = list(inv_dict)
	k = sorted(k, reverse=True)
	for i in k:
		v = sorted(inv_dict[i])
		for j in v:
			rv += j
	rv = rv[0:5]
	return rv


def decrypt_room(n, s):
	rv = ''
	for i in n:
		if i == '-':
			rv += ' '
		else:
			d = ((ord(i) - ord('a') + int(s)) % 26) + ord('a')
			rv += chr(d)
	if rv == 'northpole object storage':
		print('{}: room {}'.format(rv, s))


with (open(sys.argv[1])) as f:
	# group 1 - encrypted name
	# group 2 - sector id
	# group 3 - checksum
	p = re.compile(r'([a-z-]+)-(\d+)\[([a-z]+)\]')
	room_sum = 0
	for line in f:
		line = line.rstrip()
		m = p.match(line)
		if m:
			name = m.group(1)
			sector = m.group(2)
			check = m.group(3)
			lc = count_letters(name)
			comp = make_checksum(lc)
			if comp == check:
				room_sum += int(sector)
				decrypt_room(name, sector)
	print('sum = {}'.format(room_sum))
f.close()
