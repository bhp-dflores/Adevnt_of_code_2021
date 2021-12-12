import pandas as pd

def set_chart(contents):
    chart = pd.DataFrame(columns=[x for x in range(12)])

    pad_row = {} # I pad my frame so I don't fall out-of-bounds when flashing
    for i in range(12): pad_row[i] = '-'
    chart = chart.append(pad_row, ignore_index=True)

    for line in contents:
        line = '-'+line+'-'
        chart = chart.append(pd.Series(list(line)), ignore_index=True)
    chart = chart.append(pad_row, ignore_index=True)
    chart.iloc[1:-1,1:-1] = chart.iloc[1:-1,1:-1].astype(int)
    return chart

def flash(chart,count_tens,flashes):
    # swipe south-east from corner (1,1)
    for j in range(1,11):
        for i in range(1,11):
            if chart[i][j] > 9:
                chart[i][j] = 0
                flashes+=1
                if chart[i-1][j-1] not in ['-',0,10]: chart[i-1][j-1]=chart[i-1][j-1]+1
                if chart[i-1][j] not in ['-',0,10]: chart[i-1][j]=chart[i-1][j]+1
                if chart[i-1][j+1] not in ['-',0,10]: chart[i-1][j+1]=chart[i-1][j+1]+1
                if chart[i][j-1] not in ['-',0,10]: chart[i][j-1]=chart[i][j-1]+1
                if chart[i][j+1] not in ['-',0,10]: chart[i][j+1]=chart[i][j+1]+1
                if chart[i+1][j-1] not in ['-',0,10]: chart[i+1][j-1]=chart[i+1][j-1]+1
                if chart[i+1][j] not in ['-',0,10]: chart[i+1][j]=chart[i+1][j]+1
                if chart[i+1][j+1] not in ['-',0,10]: chart[i+1][j+1]=chart[i+1][j+1]+1
    count_tens = get_tens_count(chart)
    return chart,count_tens,flashes

def get_tens_count(chart):
    count_10s = 0
    for col in range(1,11):
        if 10 in chart[col].values:
            count_10s+=chart[col].value_counts()[10]
    return count_10s

def step(chart,flashes):
    # broadcast +1 to entire frame
    chart.iloc[1:-1,1:-1] = chart.iloc[1:-1,1:-1]+1
    count_tens = get_tens_count(chart)
    while count_tens>0:
        chart,count_tens,flashes = flash(chart,count_tens,flashes)
    return chart,flashes

if __name__=='__main__':
    #file = 'input11_test.txt'
    file = 'input11.txt'

    with open(f'inputs/{file}') as f:
        contents = f.readlines()
    contents = [x.strip() for x in contents]

    chart = set_chart(contents)

    steps = 100
    flashes = 0
    while steps > 0:
        chart,flashes = step(chart,flashes)
        steps-=1

    print(chart)
    print(f'Solution 1: {flashes} flashes after 100 steps')

    steps=100
    while chart.iloc[1:-1,1:-1].sum().sum() != 0:
        steps+=1
        chart,flashes = step(chart,flashes)

    print(chart)
    print(f"Solution 2: {steps} steps for first sync'd flash")
