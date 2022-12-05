#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 
import pandas as pd 
from io import StringIO

PATH = '/Users/liangliang/Desktop/AdventofCode2022'

def read_txt(filename):
    with open(filename) as file:
        lines = file.read().split('\n\n')
    return lines 


def solution2():
    fn = os.path.join(PATH, 'day05', 'input.txt')
    l = read_txt(fn)
    lines = l[0].split('\n')
    m, n = len(lines)-1, 9 
    stacks = [[] for _ in range(n)]
    # create stacks 
    for i in range(m):
        line = lines[i]
        cr = [line[x] for x in range(1, len(line), 4)]
        for c in range(len(cr)):
            if cr[c] != ' ':
                stacks[c].append(cr[c])
    
    stacks = [s[::-1] for s in stacks]
    # move 
    moves = l[1].split('\n')
    for j in range(len(moves)-1):
        moves_list = moves[j].split(' ')
        num, stack_from, stack_to = int(moves_list[1]), int(moves_list[3])-1, int(moves_list[5])-1
        temp = [stacks[stack_from].pop() for _ in range(num)][::-1]
        stacks[stack_to].extend(temp)

    print(''.join([x[-1] for x in stacks]))

solution2()

