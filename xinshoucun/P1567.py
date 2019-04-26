# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 19:46:21 2019

题目描述
炎热的夏日，KC 非常的不爽。他宁可忍受北极的寒冷，也不愿忍受厦门的夏天。
最近，他开始研究天气的变化。他希望用研究的结果预测未来的天气。

经历千辛万苦，他收集了连续 N天 的最高气温数据。

现在，他想知道最高气温一直上升的最长连续天数。

输入输出格式
输入格式：
第 1 行：一个整数 N[1,1000000]
 
第 2 行：N个空格隔开的整数，表示连续 N 天的最高气温。最高气温[0,1000000000]

输出格式：
1 行：一个整数，表示最高气温一直上升的最长连续天数。
"""
days = int(input())
temperatures = list(map(int, input().split()))
temperatures.append(temperatures[-1])   # every day has a tomorrow now!

ans = 0
tmp_rise_day = 1
for today in range(days):
    tomorrow = today + 1
    if temperatures[tomorrow] > temperatures[today]:
        tmp_rise_day += 1
    else:                      # stop rising     
        if tmp_rise_day > ans:
            ans = tmp_rise_day
        tmp_rise_day = 1      # reset this tmp

                     
print(ans)

