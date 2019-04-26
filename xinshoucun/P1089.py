# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:16:46 2019
津津的零花钱一直都是自己管理。每个月的月初妈妈给津津300元钱，津津会预算这个月的
花销，并且总能做到实际花销和预算的相同。

为了让津津学习如何储蓄，妈妈提出，津津可以随时把整百的钱存在她那里，到了年末她会加上
20%还给津津。因此津津制定了一个储蓄计划：每个月的月初，在得到妈妈给的零花钱后，如果她
预计到这个月的月末手中还会有多于100元或恰好100元，她就会把整百的钱存在妈妈那里
，剩余的钱留在自己手中。

例如11月初津津手中还有83元，妈妈给了津津300元。津津预计11月的花销是180
元，那么她就会在妈妈那里存200元，自己留下183元。到了11月月末，津津手中会剩下33元钱。

津津发现这个储蓄计划的主要风险是，存在妈妈那里的钱在年末之前不能取出。有可能在某个月
的月初，津津手中的钱加上这个月妈妈给的钱，不够这个月的原定预算。如果出现这种情况，津津
将不得不在这个月省吃俭用，压缩预算。

现在请你根据2004年1月到12月每个月津津的预算，判断会不会出现这种情况。如果不会，计算
到2004年年末，妈妈将津津平常存的钱加上20％还给津津之后，津津手中会有多少钱。

输入格式：
12行数据，每行包含一个小于350的非负整数，分别表示11月到12月津津的预算。

输出格式：
一个整数。如果储蓄计划实施过程中出现某个月钱不够用的情况，输出-X，X表示出现这种情况
的第一个月；否则输出到2004年年末津津手中会有多少钱。
"""


InsufficientFund = False
salary = 300
moneyInHand = 0
savings = 0
budget = 0

for imonth in range(12):
    #print('month %d begin, money = %d' %(imonth+1, moneyInHand))
    moneyInHand += salary   
    this = input().split()
    budget = int(this[0])
    moneyInHand -= budget
    #print('budget = %d, so money = %d' %(budget, moneyInHand))
    if moneyInHand < 0:
        InsufficientFund = True
        print('-%d' % (imonth + 1),end='')
        break
    elif moneyInHand >= 100:
        savings += (moneyInHand//100)*100
        moneyInHand -= (moneyInHand//100)*100
        #print('save the money,saving = %d, money = %d' %(savings,moneyInHand))
        
if InsufficientFund==False:
    moneyInHand += savings*1.2
    print('%d' %(moneyInHand),end='')

    












