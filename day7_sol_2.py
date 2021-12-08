import pandas as pd

with open('inputs/input7.txt') as f:
    contents = f.readlines()
contents = [int(x) for x in contents[0].split(',')]

# contents = [16,1,2,0,4,2,7,1,2,14]
# fuel_cost = []

# for i in range(0,max(contents)):
#     temp = []
#     for pos in contents:
#         fuel = 0
#         step = 0
#         for k in range(0,abs(pos-i)):
#             step+=1
#             fuel+=step
#         temp.append(fuel)
#     fuel_cost.append((i,sum(temp)))

# position, min_fuel = min(fuel_cost, key = lambda t: t[1])

df = pd.DataFrame({0: contents})
for i in range(1,max(contents)):
    df[i] = abs(df[0]-i)
df1 = df.copy()
del df
min_fuel_1 = min(df1.sum())

for i in range(0,max(contents)):
    for j in range(len(df1)):
        steps = 0
        fuel = 0
        for k in range(0,df1[i][j]):
            steps+=1
            fuel+=steps
        df1[i][j]=fuel
min_fuel_2 = min(df1.sum())
