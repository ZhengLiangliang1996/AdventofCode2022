#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2022 liangliang <liangliang@Liangliangs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.
import os 
import re
PATH = '/Users/liangliang/Desktop/AdventofCode2022'

def read_txt(filename):
    with open(filename) as file:
        lines = file.read().split('\n\n')
         
    return lines 


def capture_start_item(string):
    REX = re.search(r'Starting items: (.*)', string)
    l =  list(map(int, REX.group(1).strip().split(',')))
    return l 

def capture_operation(string):
    REX = re.search(r'Operation: new = (.*)', string)
    l = REX.group(1).strip()
    return l

def capture_division(string):
    REX = re.search(r'Test: divisible by (.*)', string)
    l = int(REX.group(1).strip())
    return l

def capture_true_monkey(string):
    REX = re.search(r'If true: throw to monkey (.*)', string)
    l = int(REX.group(1).strip())
    return l

def capture_false_monkey(string):
    REX = re.search(r'If false: throw to monkey (.*)', string)
    l = int(REX.group(1).strip())
    return l

def create_empty_lists(n):
    return [[] for _ in range(n)]

def solution1():
    import collections
    fn = os.path.join(PATH, 'day11', 'input.txt')
    l = read_txt(fn)
    inilize_dict = collections.defaultdict(int)
    cnt = 0
    rnd = 0
    new_stt_item = [[] for _ in range(10)]
    operations = [] 
    divisions = [] 
    true_throw = [] 
    false_throw = [] 
    while rnd < 20:
        cnt = 0
        for monkey in l:
            if monkey:
                lines = monkey.split('\n')
                if rnd == 0:
                    stt_items = capture_start_item(lines[1])
                    stt_items += new_stt_item[cnt]
                else:
                    stt_items = new_stt_item[cnt]
                
                inilize_dict[cnt] += len(stt_items)
                new_stt_item[cnt] = []
                if rnd == 0:
                    operations.append(capture_operation(lines[2]))
                    divisions.append(capture_division(lines[3]))
                    true_throw.append(capture_true_monkey(lines[4]))
                    false_throw.append(capture_false_monkey(lines[5]))
                
                for old in stt_items:
                    new = eval(operations[cnt])
                    newnew = new // 3
                    if newnew % divisions[cnt] == 0:
                        #inilize_dict[true_throw] += 1
                        new_stt_item[true_throw[cnt]].append(newnew)
                    else:
                        #inilize_dict[false_throw] += 1
                        new_stt_item[false_throw[cnt]].append(newnew)
            cnt += 1
        rnd += 1
    l = list(inilize_dict.values())
    l.sort()
    print(l[-1] * l[-2])


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



solution1()

