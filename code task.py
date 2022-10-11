# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:40:25 2022

@author: Sneha
"""

a='sneha'
print(a[:: -1])

#error and exception

try:
    a =int(input('Enter your pincode:'))
except Exception:
    print('Incorrect Pincode, please give correct format')
else:
    print('Pincode: ',a)

#code task

try:
    a = int(input('enter the 1st value:'))
    b = int(input('enter the 2st value:'))
    c = int(a/b)
    print(c)
except Exception:
    print(" invalid literal for int() with base 10: '$' 3")
else:
    print('integer division or modulo by zero')
    

T = int(input())
for i in range(T):
    a,b=map(str,input().strip().split())
try:
    print(int(a)/int(b))
except Exception as e:
    print("Error Code:",e)
    


















