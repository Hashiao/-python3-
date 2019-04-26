# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:51:38 2019

题目描述
试计算在区间 1 到 n的所有整数中，数字 x(0 ≤ x ≤ 9)共出现了多少次？例如，
在 1到11中，即在 1,2,3,4,5,6,7,8,9,10,11中，数字 1 出现了 4 次。

输入输出格式
输入格式：
2个整数n,x，之间用一个空格隔开。

输出格式：
1个整数，表示x出现的次数。
import time

time_start=time.time()
time_end=time.time()
print('totally cost',time_end-time_start)

num=1234
listll = list(map(int, str(num)))
"""
import time
input_list = input().split()

time_start=time.time()

n = int(input_list[0])
x = int(input_list[1])
x_times = 0
x_str = str(x)

for i in range(1,n+1):
    i_list = list(str(i))
    for this_num in i_list:
        if x_str==this_num:            
            x_times += 1
            
print(x_times)

time_end=time.time()
print('totally cost',time_end-time_start)



