# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:15:44 2021

@author: DavidFlores
"""

def part_a(puzzle_list):
  count = 0
  idx=1
  for depth in puzzle_list[1:]:
    if depth > puzzle_list[idx-1]:
      count += 1
    idx += 1
  return count

def part_b(puzzle_list):
  new_list = []
  for idx in range(0,len(puzzle_list)-2):
    a = puzzle_list[idx:idx+3]
    new_list.append(sum(a))
  count = part_a(new_list)
  return count

if __name__ == '__main__':
  with open('inputs/input1.txt') as f:
    contents = f.readlines()
  contents = [int(x) for x in contents]

  count_a = part_a(contents)
  count_b = part_b(contents)
