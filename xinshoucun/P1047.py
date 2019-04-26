# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:44:26 2019

题目描述
某校大门外长度为L的马路上有一排树，每两棵相邻的树之间的间隔都是1米。
我们可以把马路看成一个数轴，马路的一端在数轴0的位置，另一端在L的位置；
数轴上的每个整数点，即0,1,2,…,L，都种有一棵树。

由于马路上有一些区域要用来建地铁。这些区域用它们在数轴上的起始点和终止点表示
。已知任一区域的起始点和终止点的坐标都是整数，区域之间可能有重合的部分。
现在要把这些区域中的树（包括区域端点处的两棵树）移走。你的任务是计算将这些树都移走后，
马路上还有多少棵树。

输入输出格式
输入格式：
第一行有2个整数L[1, 10000] 和 M[1,100]，L代表马路的长度，
M代表区域的数目，L和M之间用一个空格隔开。
接下来的M行每行包含2个不同的整数，用一个空格隔开，表示一个区域的起始点和终止点的坐标。

输出格式：
1个整数，表示马路上剩余的树的数目。
"""
first_line = input().split()
L = int(first_line[0])
M = int(first_line[1])
# initialize the tree_list, 1-> tree, 0->NONE
tree_list = [1]*(L+1)   # 0 -> 100, if L==100

for area in range(M):
    this_area = input().split()
    this_start = int(this_area[0])    
    this_end = int(this_area[1])
    for i in range(this_start, this_end + 1):
        if tree_list[i]==1:    # remove this tree, if it exists
            tree_list[i] = 0
            
tree_remain = 0
for i in range(L+1):
    tree_remain += tree_list[i]

print(tree_remain)



