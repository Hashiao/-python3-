# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:47:22 2019

将1,2,⋯,9共9个数分成3组，分别组成3个三位数，且使这3个三位数构成1:2:3的比例，
试求出所有满足条件的3个三位数。
"""

def judge( num1, num2, num3 ):
    # the num can't be too large
    if num2 > 999 or num3 > 999:
        return False
    list_taken = []
    list_1 = list(str(num1))        #check if numbers are repeated
    for x in list_1:
        if x in list_taken or x=='0': # repeated, False
            return False           
        else:
            list_taken.append(x)    # new numbers, occupie these numbers
    
    list_2 = list(str(num2))       
    for x in list_2:
        if x in list_taken or x=='0':
            return False           
        else:
            list_taken.append(x)   
            
    list_3 = list(str(num3))
    for x in list_3:
        if x in list_taken or x=='0':
            return False
        else:
            list_taken.append(x)    
            
    return True

ans = []
num1 = 0
num2 = 0
num3 = 0

for i in range(100,334):
    num1 = i
    num2 = 2*i
    num3 = 3*i
    if judge(num1, num2, num3)==True:
         ans.append([num1, num2, num3])

for group in ans:   
    for number in group:
        print(number, end = ' ')   # each line ends by a space
    print()         

   

    

            
        
    



        
