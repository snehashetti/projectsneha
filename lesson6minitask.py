# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 14:30:04 2022

@author: Sneha
"""

list1 =[]
def three(number):
    if '3' in str(number):
        return number
for i in range(1, 1001):
    num = three(i)
    if num:
        list1.append(num)

a = 'welcome to python internship'
n=0
for i in a:
    if i == ' ':
        n += 1
print(n)
        

b = len([i for i in a if i == " "])
    
