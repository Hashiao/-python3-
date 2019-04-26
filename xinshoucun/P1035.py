# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:33:42 2019
调和级数，给定一个正整数K[1,15]， 需要多少级求和呢
"""

K = int(input())
sum = 0
idx = 0
while(sum <= K):
    idx = idx + 1
    sum = sum + 1/idx
    
print(idx)