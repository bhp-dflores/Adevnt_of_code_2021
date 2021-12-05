# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 11:57:44 2021

@author: DavidFlores
"""
def init_game(contents):
    "get a list of numbers to be called"
    game_nbrs = contents[0].split(',')
    game_nbrs = [int(x) for x in game_nbrs]

    "clean up double spaces in the boards"
    i = 1
    for line in contents[1:]:
        contents[i] = ' '.join(line.split())
        i+=1

    "create a dictionary of boards"
    boards_master = {}
    idx = 0
    for line in contents[1:]:
        if len(line)==0:
            boards_master[idx]=[]
            idx+=1
        elif len(line)>0:
            #line = line.split()
            line = [int(x) for x in line.split()]
            boards_master[idx-1].append(line)

    "create a dictionary to track board's performance"
    bingo_checker = {}
    for i in range(len(boards_master)):
        bingo_checker[i] = {
            'row':[0,0,0,0,0],
            'col':[0,0,0,0,0]
            }
    return game_nbrs, boards_master, bingo_checker


def play_game(nbr,boards,bingo_checker):
    """here I mark a called number-match by making it string and
    also track the board's rows and columns matches"""
    for board in boards:
        for row in boards[board]:
            x = boards[board].index(row)
            for col in row:
                if col == nbr:
                    y = row.index(col)
                    row[y] = str(nbr)
                    bingo_checker[board]['row'][x]+=1
                    bingo_checker[board]['col'][y]+=1
    return boards, bingo_checker


def bingo(winner_boards,winner_numbers,boards,bingo_checker):
    """here I pull the key of the board that just won as well as the number that made it win,
    I remove that board from the game as well as its tracker to stop marking numbers in it and
    to speed up the next check (less boards to track)"""
    for k in list(bingo_checker.keys()):
        if 5 in bingo_checker[k]['row']:
            winner_boards.append(k)
            winner_numbers.append(nbr)
            del boards[k]
            del bingo_checker[k]

        elif 5 in bingo_checker[k]['col']:
            winner_boards.append(k)
            winner_numbers.append(nbr)
            del boards[k]
            del bingo_checker[k]
    return winner_boards,winner_numbers,boards,bingo_checker


def board_score(idx,boards_master,winner_boards,winner_numbers):
    "I can get the score of any board by use of its index in the winner_boards list"
    brd_sum = 0
    for row in boards_master[winner_boards[idx]]:
        for i in row:
            if isinstance(i,int):
                brd_sum+=i

    score = brd_sum*winner_numbers[idx]
    return score


if __name__ == '__main__':
    with open('inputs/input4.txt') as f:
        contents = f.readlines()

    game_nbrs, boards_master, bingo_checker = init_game(contents)

    winner_boards = []
    winner_numbers = []
    boards = boards_master.copy()

    for nbr in game_nbrs:
        boards, bingo_checker = play_game(nbr,boards,bingo_checker)
        winner_boards,winner_numbers,boards,bingo_checker = bingo(winner_boards,winner_numbers,
                                                                  boards,bingo_checker)

    solution_1 = board_score(0,boards_master,winner_boards,winner_numbers)
    solution_2 = board_score(-1,boards_master,winner_boards,winner_numbers)
