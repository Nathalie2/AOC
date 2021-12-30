# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1]) as f:
    data = list(map(int,f.read().split(',')))

def fishtimer(days):
    for _ in range(days):
        for i in range(len(data)):
            if data[i] != 0:
                data[i]= data[i]-1
            else:
                data[i]= 6
                data.append(8)
    print(len(data))

fishtimer(80)

