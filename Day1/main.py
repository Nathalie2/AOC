# -*- coding: utf-8 -*-
#%% part 1
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

numbers = [int(line.strip()) for line in lines]

count = sum(y>x for x,y in zip(numbers[:-1], numbers[1:]))

print(count)
#%% part 2
count = sum(y>x for x,y in zip(numbers[:-3], numbers[3:]))
print(count)