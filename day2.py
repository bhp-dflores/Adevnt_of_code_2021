# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:47:16 2021

@author: DavidFlores
"""
import re

def tuple_list(list1: list)-> list:
    'creates tuple from each list item: (command(str),measure(int))'
    new_list=[]
    for item in list1:
        a_tuple = re.search(r'(\w+)\s(\d+)',item)
        new_list.append((a_tuple.group(1),int(a_tuple.group(2))))

    return new_list

def horizontal_x_depth(list1: list)-> int:
    'solves the first question'
    horizontal = 0
    depth = 0
    for item in list1:
        if 'forward' in item[0]:
            horizontal = horizontal + item[1]
        elif 'down' in item[0]:
            depth = depth + item[1]
        elif 'up' in item[0]:
            depth = depth - item[1]

    return horizontal * depth

def horizontal_x_depth2(list1: list)-> int:
    'solves the second question'
    horizontal = 0
    aim = 0
    depth = 0
    for item in list1:
        if 'forward' in item[0]:
            horizontal = horizontal + item[1]
            depth = depth + aim*item[1]
        elif 'down' in item[0]:
            aim = aim + item[1]
        elif 'up' in item[0]:
            aim = aim - item[1]

    return horizontal * depth


if __name__ == '__main__':
    with open('inputs/input2.txt') as f:
        contents = f.readlines()

    contents = tuple_list(contents)
    solution_1 = horizontal_x_depth(contents)
    solution_2 = horizontal_x_depth2(contents)
