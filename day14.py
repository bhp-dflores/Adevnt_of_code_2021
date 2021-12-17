#file = 'input14_test.txt'
file = 'input14.txt'

with open(f'inputs/{file}') as f:
    contents = f.readlines()

template = contents[0].strip()

pairs = {}
for line in contents[2:]:
    x,y = line.split('->')
    pairs[x.strip()] = x.strip()[0]+y.strip()

def insertion(template, pairs):
    new_temp = ''
    i=0
    while i < len(template)-1:
        new_temp+=pairs[template[i:i+2]]
        i+=1
    return new_temp+template[-1]

def polymer(template,pairs,steps):
    for i in range(steps): template = insertion(template,pairs)
    chars = set(template)
    frequency = {}
    for i in chars: frequency[i]= template.count(i)
    return frequency, template

def min_max(frequency):
    min_char, max_char = 0,0
    min_char, max_char = min(frequency.values()), max(frequency.values())
    return min_char, max_char

freq, template = polymer(template,pairs,10)
min_char, max_char = min_max(freq)
print(f'Solution 1: {max_char-min_char}')

freq, template = polymer(template,pairs,40)
min_char, max_char = min_max(freq)
print(f'Solution 2: {max_char-min_char}')
