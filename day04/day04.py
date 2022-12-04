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
    fn = os.path.join(PATH, 'day04', 'input.txt')
    l = read_txt(fn)
    small_sum = 0
    for i in range(len(l)):
        if l[i] != '':
            [r1, r2] = l[i].split(',')
            [r1_lo, r1_hi] = [int(x) for x in r1.split('-')]
            [r2_lo, r2_hi] = [int(x) for x in r2.split('-')]
            if (r1_lo <= r2_lo and r1_hi >= r2_hi) or (r1_lo >= r2_lo and r1_hi <= r2_hi):
                #if r1_lo == r2_lo and r1_hi == r2_hi:
                #    small_sum += 2
                #else:
                small_sum += 1
    print(small_sum)

def solution2():
    fn = os.path.join(PATH, 'day04', 'input.txt')
    l = read_txt(fn)
    small_sum = 0
    for i in range(len(l)):
        if l[i] != '':
            [r1, r2] = l[i].split(',')
            [r1_lo, r1_hi] = [int(x) for x in r1.split('-')]
            [r2_lo, r2_hi] = [int(x) for x in r2.split('-')]
            lo = max(r1_lo, r2_lo)
            hi = min(r1_hi, r2_hi)
            if lo <= hi:
                small_sum += 1
    print(small_sum)



solution2()

