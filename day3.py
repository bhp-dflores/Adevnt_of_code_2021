# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:58:31 2021

@author: DavidFlores
"""
def gamma_epsilon(a_list):
    gamma = []
    for x in range(len(a_list[0])):
        gamma.append(0)
    for number in a_list:
        for i in range(len(number)):
            gamma[i]+=int(number[i])
    for i in range(len(gamma)):
        if gamma[i] >= (len(a_list)/2):
            gamma[i] = 1
        else:
            gamma[i] = 0
    gamma = [str(x) for x in gamma]
    epsilon = ['1' if x == '0' else '0' for x in gamma]
    return gamma, epsilon

def oxygen(a_list):
    gam, eps = gamma_epsilon(a_list)
    lista = a_list.copy()
    listb = []
    i = 0
    while i < len(lista[0]) and len(lista)!=1:
        for x in lista:
            if len(lista) == 2:
                if lista[0][i] == '1':
                    listb.append(lista[0])
                else:
                    listb.append(lista[1])
            elif x[i] == gam[i]:
                listb.append(x)
        lista = listb.copy()
        listb.clear()
        gam, eps = gamma_epsilon(lista)
        i+=1
    return int(lista[0],2)

def co2(a_list):
    gam, eps = gamma_epsilon(a_list)
    lista = a_list.copy()
    listb = []
    i = 0
    while i < len(lista[0]) and len(lista)!=1:
        for x in lista:
            if len(lista) == 2:
                if lista[0][i] == '0':
                    listb.append(lista[0])
                else:
                    listb.append(lista[1])
            elif x[i] == eps[i]:
                listb.append(x)
        lista = listb.copy()
        listb.clear()
        gam, eps = gamma_epsilon(lista)
        i+=1
    return int(lista[0],2)

if __name__ == '__main__':
    # with open('inputs/input3_test.txt') as f:
    with open('inputs/input3.txt') as f:
        contents = f.readlines()
    contents = [x.strip() for x in contents]

    gam, eps = gamma_epsilon(contents)

    solution_1 = int(''.join(gam),2) * int(''.join(eps),2)
    solution_2 = oxygen(contents) * co2(contents)
