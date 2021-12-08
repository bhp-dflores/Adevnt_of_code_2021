# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 13:23:01 2021

@author: DavidFlores
"""

from collections import Counter

def fish_count(contents, days):
    count_contents = Counter(contents)

    count_age = {}
    for i in range(9):
        count_age[i]=count_contents[i]

    new=0
    for i in range(days):
        if count_age[0] >= 1:
            new = count_age[0]
        for i in range(0,8):
            count_age[i]=count_age[i+1]
        count_age[6]+=new
        count_age[8]=new
        new=0
    return sum(count_age.values())

with open('inputs/input6.txt') as f:
    contents = f.readlines()
contents = [int(x) for x in contents[0].split(',')]

nbr_fish1 = fish_count(contents, 80)
nbr_fish2 = fish_count(contents, 256)
