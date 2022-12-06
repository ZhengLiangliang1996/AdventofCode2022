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

# Function to check if all characters in a string are different
def are_all_different(s):
    s_set = set(s)
    return len(s_set) == len(s)

# Test the subroutine with the given datastream buffer
def solution1():
    fn = os.path.join(PATH, 'day06', 'input.txt')
    l = read_txt(fn)
    temp = ''
    cnt = 0
    while True:
        if len(temp) < 14:
            temp += l[0][cnt]
            cnt += 1
        elif len(temp) == 14:
            if are_all_different(temp):
                break
            else:
                temp = temp[1:]
    print(cnt)

solution1()

