# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:37:50 2019

小玉开心的在游泳，可是她很快难过的发现，自己的力气不够，游泳好累哦。
已知小玉第一步能游2米，可是随着越来越累，力气越来越小，她接下来的每一步都只能游出上
一步距离的98%。现在小玉想知道，如果要游到距离x米的地方，她需要游多少步呢。请你编程
解决这个问题。

输入输出格式
输入格式：
输入一个数字（不一定是整数，小于100m），表示要游的目标距离。

输出格式：
输出一个整数，表示小玉一共需要游多少步。
"""

distance = float(input())
first_step = 2
sum_distance = 0
step = 0
while(sum_distance < distance):
    sum_distance += first_step*pow(0.98, step)
    step += 1
    
print(step)

