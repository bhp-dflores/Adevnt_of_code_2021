# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 00:28:08 2021

@author: DavidFlores
"""
import re

def create_screen(size):
    screen = []
    screen_c = []
    for i in range(size):
        for j in range(size):
            screen_c.append(0)
        screen_r = screen_c.copy()
        screen.append(screen_r)
        screen_c.clear()
    return screen

def up_down(screen,new_contents):
    for coord in new_contents:
        x1,y1 = coord[0][0], coord[0][1]
        x2,y2 = coord[1][0], coord[1][1]
        if y1 == y2:
            if x2>x1:
                for x in range(x1,x2+1):
                    screen[y1][x]+=1
            else:
                for x in range(x2,x1+1):
                    screen[y1][x]+=1
        elif x1 == x2:
            if y2>y1:
                for y in range(y1,y2+1):
                    screen[y][x1]+=1
            else:
                for y in range(y2,y1+1):
                    screen[y][x1]+=1
    return screen

def diags(screen,new_contents):
    for coord in new_contents:
        x1,y1 = coord[0][0], coord[0][1]
        x2,y2 = coord[1][0], coord[1][1]
        if x2>x1 and y1 != y2:
            if y2>y1:
                for x in range(x1,x2+1):
                    screen[y1][x]+=1
                    y1+=1
            else:
                for x in range(x1,x2+1):
                    screen[y1][x]+=1
                    y1-=1
        elif x1>x2 and y1 != y2:
            if y2>y1:
                for x in range(x2,x1+1):
                    screen[y2][x]+=1
                    y2-=1
            else:
                for x in range(x2,x1+1):
                    screen[y2][x]+=1
                    y2+=1
    return screen

def points(screen):
    count = 0
    for row in screen:
        for i in row:
            if i >= 2:
                count+=1
    return count

if __name__ == '__main__':
    with open('inputs/input5.txt') as f:
        contents = f.readlines()
    new_contents = []
    for line in contents:
        a_tuple = re.search(r'(\d+,\d+)\s\-\>\s(\d+,\d+)',line)
        x1,y1 = [int(x) for x in a_tuple.group(1).split(',')]
        x2,y2 = [int(x) for x in a_tuple.group(2).split(',')]
        line = [[x1,y1],[x2,y2]]
        new_contents.append(line)
    screen = create_screen(1000)
    screen = up_down(screen, new_contents)

    solution_1 = points(screen)

    screen = diags(screen,new_contents)

    solution_2 = points(screen)
