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
    fn = os.path.join(PATH, 'day03', 'input.txt')
    l = read_txt(fn)
    small_sum = 0
    for i in range(len(l)):
        if l[i] != '':
            length = int(len(l[i])/2)
            r1, r2 = l[i][:length], l[i][length:]
            inter = list(set([x for x in r1]).intersection(set([x for x in r2])))
            for it in inter:
                if ord('a') <= ord(it) <= ord('z'):
                    small_sum += ord(it) - ord('a') + 1
                elif ord('A') <= ord(it) <= ord('Z'):
                    small_sum += ord(it) - ord('A') + 27
    print(small_sum)

def solution2():
    fn = os.path.join(PATH, 'day03', 'input.txt')
    l = read_txt(fn)
    small_sum = 0
    small_l = []
    g = [l[i*3:i*3+3] for i in range(0, int(len(l)/3))]
    for i in range(len(g)):
        if l[i] != '':
            r1, r2, r3 = g[i][0], g[i][1], g[i][2]
            inter = list(set([x for x in r1]).intersection(set([x for x in r2])))
            inter = list(set([x for x in r3]).intersection(set([x for x in inter])))
            for it in inter:
                if ord('a') <= ord(it) <= ord('z'):
                    small_sum += ord(it) - ord('a') + 1
                elif ord('A') <= ord(it) <= ord('Z'):
                    small_sum += ord(it) - ord('A') + 27
    print(small_sum)


solution2()

