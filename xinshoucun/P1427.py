# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:33:13 2019

小鱼最近被要求参加一个数字游戏，要求它把看到的一串数字（
长度不一定，以0结束，最多不超过100个，数字不超过2^32-1），
记住了然后反着念出来(表示结束的数字0就不要念出来了)。
这对小鱼的那点记忆力来说实在是太难了，你也不想想小鱼的整个脑袋才多大，
其中一部分还是好吃的肉！所以请你帮小鱼编程解决这个问题。

输入输出格式
输入格式：
一行内输入一串整数，以0结束，以空格间隔。

输出格式：
一行内倒着输出这一串整数，以空格间隔。
"""

input_list = input().split()
num_list = list(map(int, input_list))
# find the first zero
idx = 0
for num in num_list:
    if num == 0:
        break
    else:
        idx += 1

# reverse print from idx-1 to 0
for i in range(idx-1,-1,-1):
    print(num_list[i], end = ' ')

