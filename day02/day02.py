#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 

PATH = '/Users/liangliang/Desktop/AdventofCode2022'

def read_txt(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
         
    return lines 

def solution1():
    fn = os.path.join(PATH, 'day02', 'input.txt')
    l = read_txt(fn)
    small_sum = 0
    strategy_score = {'Y': 2, 'X': 1, 'Z': 3}
    possibility = [('A', 'Y', 6), ('B', 'X', 0), ('C', 'Z', 3),
                   ('A', 'X', 3), ('B', 'Y', 3), ('C', 'Y', 0),
                   ('A', 'Z', 0), ('B', 'Z', 6), ('C', 'X', 6)]
    for i in range(len(l)):
        if l[i] == '':
            continue
        [opponent, strategy] = l[i].split(' ')
        for p in range(len(possibility)):
            if possibility[p][0] == opponent and possibility[p][1] == strategy:
                small_sum += possibility[p][2]
                small_sum += strategy_score[strategy]
                break
    print(small_sum)
def solution2():
    fn = os.path.join(PATH, 'day02', 'input.txt')
    l = read_txt(fn)
    small_sum = 0
    strategy_score = {'B': 2, 'A': 1, 'C': 3}
    winning_score = {'Y': 3, 'X': 0, 'Z':6}
    possibility = [('A', 'Y', 'A'), ('B', 'X', 'A'), ('C', 'Z', 'A'),
                   ('A', 'X', 'C'), ('B', 'Y', 'B'), ('C', 'Y', 'C'),
                   ('A', 'Z', 'B'), ('B', 'Z', 'C'), ('C', 'X', 'B')]
    for i in range(len(l)):
        if l[i] == '':
            continue
        [opponent, strategy] = l[i].split(' ')
        for p in range(len(possibility)):
            if possibility[p][0] == opponent and possibility[p][1] == strategy:
                small_sum += winning_score[possibility[p][1]]
                small_sum += strategy_score[possibility[p][2]]
                break
    print(small_sum)

solution2()

