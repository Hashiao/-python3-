# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:06:09 2019

题目描述
P老师需要去商店买n支铅笔作为小朋友们参加NOIP的礼物。她发现商店一共有 3种包装的铅笔，
不同包装内的铅笔数量有可能不同，价格也有可能不同。为了公平起见，P老师决定只买同一种包
装的铅笔。

商店不允许将铅笔的包装拆开，因此P老师可能需要购买超过n支铅笔才够给小朋 友们发礼物。

现在P老师想知道，在商店每种包装的数量都足够的情况下，要买够至少n支铅笔最少需要花费多
少钱。

输入输出格式
输入格式：
第一行包含一个正整数n，表示需要的铅笔数量。

接下来三行，每行用2个正整数描述一种包装的铅笔：其中第1个整数表示这种 包装内铅笔的数量
，第2个整数表示这种包装的价格。

保证所有的7个数都是不超过10000的正整数。

输出格式：
1个整数，表示P老师最少需要花费的钱。
"""
import math
num_need = input()
num_need = int(num_need)

price = [0]*3
num_pencil = [0]*3
moneycost = -1;

for i in range(3):
    this = input().split()
    num_pencil[i] = int(this[0])
    price[i] = int(this[1])
    thismoneycost = math.ceil(num_need/num_pencil[i]) * price[i]
    if (thismoneycost < moneycost) or (moneycost < 0) :
        moneycost = thismoneycost

print(moneycost)
    














