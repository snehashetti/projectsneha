# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 10:19:00 2022

@author: Sneha
"""
#shop1
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
list1=[]
for item in orders:
    if item[-1]*item[-2] < 100:
        list1.append((item[0], item[-1]*item[-2]+10))
    else:
        list1.append((item[0], item[-1]*item[-2]))

#temperature
"""
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius = []
for temp in fahrenheit:
    a =((fahrenheit[temp] - 32)*5)/9
    celsius.append(a)
    """
    
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius=list(map(lambda temp:(((temp - 32)*5)/9), fahrenheit.values() ))

cel_dict = dict(zip(fahrenheit.keys(), celsius))
print(cel_dict)