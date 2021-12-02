# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

numbers = [int(line.strip()) for line in lines]

count = sum(y>x for x,y in zip(numbers[:-1], numbers[1:]))

print(count)