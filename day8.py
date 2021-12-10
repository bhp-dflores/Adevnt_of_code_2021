import pandas as pd
file = 'input8.txt'
#file = 'input8_test.txt'

with open(f'inputs/{file}') as f:
    contents = f.readlines()
contents = [x.split('|') for x in contents]

for i in range(len(contents)):
    for j in [0,1]:
        contents[i][j] = contents[i][j].strip().split(' ')

output_lens = []
for line in contents:
    output_lengths = [len(x) for x in line[1]]
    output_lens.append(output_lengths)

count=0
for item in output_lens:
    count+=len([x for x in item if x in (2,3,4,7)])

print(f'Solution 1: {count}')

decoder = pd.DataFrame(columns=[x for x in range(10)])

for line in contents:
    test = line[0].copy()
    code = {}
    # find 1,4,7 and 8
    code[1] = [i for i in test if len(i)==2][0]
    test.remove(code[1])
    code[4] = [i for i in test if len(i)==4][0]
    test.remove(code[4])
    code[7] = [i for i in test if len(i)==3][0]
    test.remove(code[7])
    code[8] = [i for i in test if len(i)==7][0]
    test.remove(code[8])
    # find 3,6,9
    code[3] = [i for i in test if len(set(i) - set(code[7])) == 2][0]
    test.remove(code[3])
    code[6] = [i for i in test if len(set(i) - set(code[7])) == 4][0]
    test.remove(code[6])
    code[9] = [i for i in test if set(i) == set(code[3]+code[4])][0]
    test.remove(code[9])
    # find 5
    segment = set(code[8]) - set(code[9])
    code[5] = [i for i in test if set(i) == (set(code[6]) - segment)][0]
    test.remove(code[5])
    # find 2 and 0
    code[0] = [i for i in test if len(i) == 6][0]
    code[2] = [i for i in test if len(i) == 5][0]

    test_output=line[1].copy()
    out=[]
    for i in range(4):
        for j in code:
            if set(test_output[i]) == set(code[j]):
                out.append(str(j))
    code['output'] = int(''.join(out))
    decoder = decoder.append(code, ignore_index=True)

suma = sum(decoder['output'])

print(f"solution 2: {suma}")
