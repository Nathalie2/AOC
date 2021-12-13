# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

def part1():
    grid = defaultdict(int)
    for line in data:
        start, end = [list(map(int,y.split(','))) for y in line.split(' -> ')]
        if start[0] == end[0]:
            y = list(range(start[-1], end[-1]+1)) if len(list(range(start[-1], end[-1]+1))) !=0 else list(range(end[-1], start[-1]+1))
            x = [start[0]]*len(y)
            for i,j in zip(x,y):
                grid[(i,j)] +=1
        elif start[-1] == end[-1]:
            x = list(range(start[0], end[0]+1)) if len(list(range(start[0], end[0]+1))) !=0 else list(range(end[0], start[0]+1))
            y = [start[-1]]*len(x)
            for i,j in zip(x,y):
                grid[(i,j)] +=1
    print(sum(value>1 for value in grid.values()))

part1()