# -*- coding: utf-8 -*-
#%% part 1
import pandas as pd
import sys

df = pd.read_csv(sys.argv[1], delimiter = ' ', header=None, names = ['direction', 'step'])

hor_pos = df['step'][df['direction']=='forward'].sum()
depth = df['step'][df['direction']=='down'].sum() - df['step'][df['direction']=='up'].sum()

answer = hor_pos*depth
print(answer)
#%% part 2
hor_pos = 0
aim = 0
depth = 0

for index in df.index:
    if df.loc[index,'direction']=='forward':
        hor_pos += df.loc[index,'step']
        depth += aim * df.loc[index,'step']
    elif df.loc[index,'direction']=='down':
        aim += df.loc[index,'step']
    elif df.loc[index,'direction']=='up':
        aim -= df.loc[index,'step']

answer = hor_pos * depth
print(answer)
