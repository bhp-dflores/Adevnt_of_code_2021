import pandas as pd
from math import prod

file = 'input9.txt'
#file = 'input9_test.txt'

with open(f'inputs/{file}') as f:
    contents = f.readlines()

for i in range(len(contents)):
    contents[i] = list('9'+contents[i].strip()+'9')

row = {i:'9' for i in range(len(contents[0]))}

plot = pd.DataFrame().append(row, ignore_index=True)

for i in range(len(contents)):
    new_row = pd.Series(contents[i], index = plot.columns)
    plot = plot.append(new_row, ignore_index=True)
plot = plot.append(row, ignore_index=True)
plot = plot.astype(int)

lows=[]

for j in range(1,len(plot)-1): #rows
    for i in range(1, len(contents[0])-1): #columns
        if plot[i][j] < plot[i][j-1] and plot[i][j] < plot[i][j+1] \
            and plot[i][j] < plot[i-1][j] and plot[i][j] < plot[i+1][j]:
                lows.append(plot[i][j])

risk_level = sum(lows)+(1*len(lows))
print(f'Solution 1: {risk_level}')

df = plot.copy().astype(str)

bsn_cnt = 1
basin = {}
for j in range(1,len(plot)-1): #rows
    for i in range(1, len(contents[0])-1): #columns
        if plot[i][j] < plot[i][j-1] and plot[i][j] < plot[i][j+1] \
            and plot[i][j] < plot[i-1][j] and plot[i][j] < plot[i+1][j]:
                df[i][j] = {'value': df[i][j], 'basin': bsn_cnt, 'count': 1}
                basin[bsn_cnt]=1
                bsn_cnt+=1

#count of values different than 9 and not a low
left_behind = sum(plot[plot != 9].count())-len(lows)

def walk_frame(df, left_behind):
    for j in range(1,len(plot)-1): #rows
        for i in range(1, len(contents[0])-1): #columns
            if df[i][j] != '9':
                if 'basin' not in df[i][j]:
                    if 'basin' in df[i][j-1]: #up
                        basin[df[i][j-1]['basin']]+=1
                        df[i][j] = {'value': df[i][j], 'basin': df[i][j-1]['basin'], 'count': basin[df[i][j-1]['basin']]}
                        left_behind-=1
                    elif 'basin' in df[i+1][j]: #right
                        basin[df[i+1][j]['basin']]+=1
                        df[i][j] = {'value': df[i][j], 'basin': df[i+1][j]['basin'], 'count': basin[df[i+1][j]['basin']]}
                        left_behind-=1
                    elif 'basin' in df[i][j+1]: #down
                        basin[df[i][j+1]['basin']]+=1
                        df[i][j] = {'value': df[i][j], 'basin': df[i][j+1]['basin'], 'count': basin[df[i][j+1]['basin']]}
                        left_behind-=1
                    elif 'basin' in df[i-1][j]: #left
                        basin[df[i-1][j]['basin']]+=1
                        df[i][j] = {'value': df[i][j], 'basin': df[i-1][j]['basin'], 'count': basin[df[i-1][j]['basin']]}
                        left_behind-=1
    return df, left_behind

while left_behind != 0:
    df, left_behind = walk_frame(df, left_behind)

three_largest_basin_values = list(basin.values())
three_largest_basin_values.sort()
three_largest_basin_values = three_largest_basin_values[-3:]

solution_2 = prod(three_largest_basin_values)
print(f'Solution 2: {solution_2}')
