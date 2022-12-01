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
    fn = os.path.join(PATH, 'day01', 'input.txt')
    l = read_txt(fn)
    max_num = -1
    small_sum = 0 
    for i in range(len(l)):
        if l[i] != '':
            small_sum += int(l[i])
        else:
            max_num = max(max_num, small_sum)
            small_sum = 0
    print(max(max_num, small_sum))

def solution2():
    fn = os.path.join(PATH, 'day01', 'input.txt')
    l = read_txt(fn)

    num = []
    small_sum = 0 
    for i in range(len(l)):
        if l[i] != '':
            small_sum += int(l[i])
        else:
            num.append(small_sum)
            small_sum = 0
    num.sort()
    print(sum(num[-3:]))

solution2()

