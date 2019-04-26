# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:22:04 2019

题目描述
津津上初中了。妈妈认为津津应该更加用功学习，所以津津除了上学之外，还要参加妈妈为她报
名的各科复习班。另外每周妈妈还会送她去学习朗诵、舞蹈和钢琴。但是津津如果一天上课超过
八个小时就会不高兴，而且上得越久就会越不高兴。假设津津不会因为其它事不高兴，并且她的
不高兴不会持续到第二天。请你帮忙检查一下津津下周的日程安排，看看下周她会不会不高兴；
如果会的话，哪天最不高兴。

输入输出格式
输入格式：
输入包括7行数据，分别表示周一到周日的日程安排。每行包括两个小于10的非负整数，用
空格隔开，分别表示津津在学校上课的时间和妈妈安排她上课的时间。

输出格式：
一个数字。如果不会不高兴则输出00，如果会则输出最不高兴的是周几（用1, 2, 3, 4, 5, 6,
 7分别表示周一，周二，周三，周四，周五，周六，周日）。如果有两天或两天
 以上不高兴的程度相当，则输出时间最靠前的一天。
"""


Sad = False
MostSadDay = -1;
LongestHour = -1;
for i in range(7):
    this = input().split()
    today_hours = int(this[0]) + int(this[1])
    if today_hours > 8:
        if Sad == False:   # first unhappy day
            Sad = True
            MostSadDay = i+1
            LongestHour = today_hours
        else:              # comparing to the former unhappy day
            if today_hours > LongestHour:
                MostSadDay = i+1
                LongestHour = today_hours
if Sad:
    print(MostSadDay)
else:
    print('00') 
   
    

