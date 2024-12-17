#!/usr/bin/env python3
# AdventOfCode 2016 Day 16


LEN = 272
#LEN = 35651584
INPUT = '11100010111110100'


def pairwise(it):
    a = iter(it)
    return zip(a, a)


def xvi_reverse(x):
    y = x[::-1]
    return y


def xvi_copy(x):
    y = list(x)
    return y


def xvi_inverse(x):
    y = []
    for n in x:
        if n == '0':
            y.append('1')
        else:
            y.append('0')
    return y


def xvi_process(x):
    copy_data = xvi_copy(x)
    rev_data = xvi_reverse(x)
    inv_data = xvi_inverse(rev_data)
    res = copy_data + ['0'] + inv_data
    return res


def xvi_checksum(x):
    done = False
    data_in = x
    while not done:
        csum = []
        for a, b in pairwise(data_in):
            if a == b:
                csum.append('1')
            else:
                csum.append('0')
        if len(csum) % 2 == 1:
            done = True
        data_in = csum
    return csum


data = list(INPUT)
while len(data) < LEN:
    data = xvi_process(data)
data = data[:LEN]
csum = xvi_checksum(data)
csum_str = ''.join(csum)
print('checksum = {}'.format(csum_str))


