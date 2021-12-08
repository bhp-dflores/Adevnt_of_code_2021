import pandas as pd

with open('inputs/input7.txt') as f:
    contents = f.readlines()
contents = [int(x) for x in contents[0].split(',')]

fuel_cost = []

df = pd.DataFrame({'position': contents})
for i in range(0,max(contents)):
    df[i] = abs(df['position']-i)
min_fuel = min(df.sum())
