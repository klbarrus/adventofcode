#!/usr/bin/env python3
# AdventOfCode 2016 Day 07

import sys
import re

# regex for the abba sequence
abba = r'([a-z])([a-z])\2\1'
p_abba = re.compile(abba)

# regex for the hypernet sequence
hyper = r'\[([a-z]+)\]'
p_hyper = re.compile(hyper)

# regex for the aba/bab sequence
# using lookahead to handle possible overlap
# e.g. 'abaca' should find 'aba' and 'aca'
aba = r'(?=([a-z])([a-z])\1)'
p_aba = re.compile(aba)


def seq_present(seq, regex):
    rv = False
    for s in seq:
        m_seq = regex.findall(s)
        if m_seq:
            for ma in m_seq:
                if ma[0] != ma[1]:
                    rv = True       # valid sequence found
                else:
                    pass
        else:
            pass
    return rv


def valid_aba(seqa, seqb):
    rv = False
    for ia in seqa:
        m_seqa = p_aba.findall(ia)
        if m_seqa:
            for ib in seqb:
                m_seqb = p_aba.findall(ib)
                if m_seqb:
                    for ma in m_seqa:
                        for mb in m_seqb:
                            if ma[0] == mb[1] and ma[1] == mb[0] and ma[0] != ma[1] and mb[0] != mb[1]:
                                rv = True
                else:
                    pass
        else:
            pass
    return rv


num_tls = 0
num_ssl = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()

        m_hyper = p_hyper.findall(line)
        m_super = set(p_hyper.split(line)) - set(m_hyper)

        b_hyper = seq_present(m_hyper, p_abba)
        b_super = seq_present(m_super, p_abba)
        if not b_hyper and b_super:
            num_tls += 1

        b_hyper = seq_present(m_hyper, p_aba)
        b_super = seq_present(m_super, p_aba)
        if b_hyper and b_super:
            if valid_aba(m_super, m_hyper):
                num_ssl += 1
f.close()

print('num tls: {}'.format(num_tls))
print('num ssl: {}'.format(num_ssl))

