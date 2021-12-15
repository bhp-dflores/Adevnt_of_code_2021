#file = 'input13_test.txt'
file = 'input13.txt'

import pandas as pd


def init_paper(contents):
    dots=[]
    folds = []

    for lines in contents:
        if 'fold' not in lines and len(lines.strip())>0:
            x,y = lines.strip().split(',')
            dots.append((int(x),int(y)))
        elif len(lines.strip())>0:
            folds.append(lines.strip().split('='))

    max_x, max_y = 0,0
    for pair in dots: max_x, max_y = max(max_x,pair[0]), max(max_y,pair[1])

    paper = pd.DataFrame(columns=[i for i in range(0,max_x+1)])
    row={}
    for i in paper.columns: row[i] = '.'

    for i in range(0,max_y+1): paper = paper.append(row, ignore_index=True)

    for pair in dots: paper[pair[0]][pair[1]] = '#'

    #folds
    for fold in folds:
        fold[0] = 'x' if 'x' in fold[0] else 'y'
        fold[1] = int(fold[1])
    return paper,max_x,max_y,folds

def y_fold(paper, fold_y, max_y):
    folded=paper.loc[:fold_y-1 , :].copy()
    step = 1
    for y1 in range(fold_y+1, max_y+1):
        y2 = fold_y-step
        for x in folded.columns:
            if folded[x][y2] == '.':
                folded[x][y2] = paper[x][y1]
        step+=1
    new_max_y = folded.shape[0]-1
    return folded, new_max_y

def x_fold(paper, fold_x, max_x):
    folded=paper.loc[: , :fold_x-1].copy()
    step = 1
    for x1 in range(fold_x+1, max_x+1):
        x2 = fold_x-step
        for y, row in folded.iterrows():
            if folded[x2][y] == '.':
                folded[x2][y] = paper[x1][y]
        step+=1
    new_max_x = folded.shape[1]-1
    return folded, new_max_x


if __name__=='__main__':
    with open(f'inputs/{file}') as f:
        contents = f.readlines()

    paper,max_x,max_y,folds = init_paper(contents)

    folded = paper.copy()
    for fold in folds:
        if fold[0] == 'x':
            folded,max_x = x_fold(folded, fold[1], max_x)
        else:
            folded,max_y = y_fold(folded, fold[1], max_y)

        if fold == folds[0]:
            count_hashtag = 0
            for i in folded.columns:
                if '#' in folded[i].values:
                    count_hashtag += folded[i].value_counts()['#']
            print(f'Solution 1: {count_hashtag}')
    print(f'Solution 2:\n{folded}')
