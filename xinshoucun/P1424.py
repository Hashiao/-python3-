# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:43:37 2019

题目背景
原来的题目太简单，现改进让小鱼周末也休息，请已经做过重做该题。

题目描述
有一只小鱼，它上午游泳150公里，下午游泳100公里，晚上和周末都休息（实行双休日)，
假设从周x(1<=x<=7)开始算起，请问这样过了n天以后，小鱼一共累计游泳了多少公里呢？

输入输出格式
输入格式：
输入两个整数x,n(表示从周x算起，经过n天，n在long int范围内）。

输出格式：
输出一个整数，表示小鱼累计游泳了多少公里。
"""

input_list = input().split()
idx_week = int(input_list[0])
days = int(input_list[1])
swim_per_day = 250
already_swim = 0

for thisday in range(days):   # 0,1,2,...,9 if days == 10
    if idx_week == 8:
        idx_week = 1
    if idx_week == 6 or idx_week == 7:
        idx_week += 1
        continue
    else:
        already_swim += swim_per_day
        idx_week += 1
    
print(already_swim)
    
    


