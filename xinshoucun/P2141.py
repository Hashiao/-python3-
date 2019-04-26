# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 18:51:12 2019
题目描述
珠心算是一种通过在脑中模拟算盘变化来完成快速运算的一种计算技术。
珠心算训练，既能够开发智力，又能够为日常生活带来很多便利，因而在很多学校得到普及。

某学校的珠心算老师采用一种快速考察珠心算加法能力的测验方法。
他随机生成一个正整数集合，集合中的数各不相同，然后要求学生回答：其中有多少个数，
恰好等于集合中另外两个（不同的）数之和？

最近老师出了一些测验题，请你帮忙求出答案。

(本题目为2014NOIP普及T1)

输入输出格式
输入格式：
共两行
第一行包含一个整数n，表示测试题中给出的正整数个数。
第二行有n个正整数，每两个正整数之间用一个空格隔开，表示测试题中给出的正整数。

输出格式：
一个整数，表示测验题答案。
"""

elem_num = int(input())
num_list = list(map(int, input().split()))
ans_list = []
for first_num in range(elem_num):
    for sec_num in range(first_num+1, elem_num):
        sum = num_list[first_num]+num_list[sec_num]
        # the sum_num exsit in num_list for the first time
        if (sum in num_list) and (sum not in ans_list): 
            # record this number
            ans_list.append(num_list[first_num]+num_list[sec_num])
            
print(len(ans_list))
            


