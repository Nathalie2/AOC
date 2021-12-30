# -*- coding: utf-8 -*-
import sys
from collections import Counter

with open(sys.argv[1]) as f:
    data = list(map(int,f.read().split(',')))

def fishtimer_part1(days):
    for _ in range(days):
        for i in range(len(data)):
            if data[i] != 0:
                data[i]= data[i]-1
            else:
                data[i]= 6
                data.append(8)
    print(len(data))

fishtimer_part1(80)

with open(sys.argv[1]) as f:
    data = list(map(int,f.read().split(',')))

def fishtimer_part2(days):
    old_data = Counter(data)
    for _ in range(days):
        new_data = Counter()
        for day, count in old_data.items():
            if day != 0:
                new_data[day-1] += old_data[day]
            else:
                new_data[6] += old_data[day]
                new_data[8] += old_data[day]
        old_data = new_data
    print(sum(old_data.values()))

fishtimer_part2(256)
