# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:01:04 2019
题目描述
伦敦奥运会要到了，小鱼在拼命练习游泳准备参加游泳比赛，可怜的小鱼并不知道鱼类是不能
参加人类的奥运会的。

这一天，小鱼给自己的游泳时间做了精确的计时（本题中的计时都按24小时制计算），它发现
自己从a时b分一直游泳到当天的c时d分，请你帮小鱼计算一下，它这天一共游了多少时间呢？

小鱼游的好辛苦呀，你可不要算错了哦。

输入输出格式
输入格式：
一行内输入 4 个整数，分别表示 a, b, c, d。

输出格式：
一行内输出 2 个整数 e 和 f，用空格间隔，依次表示小鱼这天一共游了多少小时多少分钟。
其中表示分钟的整数 f 应该小于60。
"""
input_str = input().split()
a = int(input_str[0])
b = int(input_str[1])
c = int(input_str[2])
d = int(input_str[3])
hour = c - a
minute = d - b
if minute < 0:
    minute += 60
    hour -= 1
 
print('%d %d' %(hour,minute),end = '')