from statistics import median

#file = 'input10_test.txt'
file = 'input10.txt'

with open(f'inputs/{file}') as f:
    contents = f.readlines()
contents = [x.strip() for x in contents]

score_bads = {')':3,']':57,'}':1197,'>':25137}

legal = {'(':')', '[':']', '{':'}', '<':'>'}

incompletes = []
corrupts = []
for line in contents:
    openers = []
    for char in line:
        if char in legal.keys(): openers.append(char)
        else:
            if char == legal[openers[-1]]: openers.pop()
            else:
                corrupts.append(char)
                openers = []
                break
    if len(openers) != 0: incompletes.append(''.join(openers))

suma = 0
for i in corrupts:
    suma = suma + score_bads[i]

print(f'solution 1 = {suma}')

score_goods = {')':1,']':2,'}':3,'>':4}

auto_comps = []
for item in incompletes:
    score = 0
    for char in item[::-1]: #iterate the string but in reverse
        score = score*5 + score_goods[legal[char]]
    auto_comps.append(score)

print(f'solution 2 = {median(auto_comps)}')
