# -*- coding: utf-8 -*-
#%% part 1
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

strings = [line.strip() for line in lines]

t_strings = [''.join(s) for s in zip(*strings)]

gamma_bin = ''.join(['0' if nr.count('0') > nr.count('1') else '1'  for nr in t_strings])
gamma_dec = int(gamma_bin,2)

epsilon_bin = ''.join(['1' if nr.count('0') > nr.count('1') else '0'  for nr in t_strings])
epsilon_dec = int(epsilon_bin,2)

print(gamma_dec*epsilon_dec)
#%% part 2
def ox_gen(strings, nr=0):
    if len(strings) == 1:
        return int(strings[0], 2)
    t_strings = [''.join(s) for s in zip(*strings)]
    most_common = '0' if t_strings[nr].count('0') > t_strings[nr].count('1') else '1'

    return ox_gen([x for x in strings if x[nr]==str(most_common)], nr+1)

def co_gen(strings, nr=0):
    if len(strings) == 1:
        return int(strings[0], 2)
    t_strings = [''.join(s) for s in zip(*strings)]
    most_common = '0' if t_strings[nr].count('0') <= t_strings[nr].count('1') else '1'

    return co_gen([x for x in strings if x[nr]==str(most_common)], nr+1)

print(ox_gen(strings)*co_gen(strings))