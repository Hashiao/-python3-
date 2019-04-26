# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:24:43 2019
题目描述
班主任给小玉一个任务，到文具店里买尽量多的签字笔。已知一只签字笔的价格是1元9角，
而班主任给小玉的钱是a元b角，小玉想知道，她最多能买多少只签字笔呢。

输入输出格式
输入格式：
输入的数据，在一行内，包括两个整数，依次表示a和b，a<=10000,b<=9。

输出格式：
输出一个整数，表示小玉最多能买多少只签字笔。
"""
s = input().split()
a = int(s[0])   #yuan
b = int(s[1])   #jiao
#print('%d元%d角' %(a,b))
money = 10*a + b  # num of jiao
price = 19
print(money//price)

