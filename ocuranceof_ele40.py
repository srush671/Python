# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:55:03 2023

@author: srushti
"""

def count(mylist, x):
    return mylist.count(x)
 
 
mylist = [8, 6, 8, 10, 8, 20, 10, 8, 8]

n = int(input("Enter Number You want to Check"))
print('{} has occurred {} times'.format(n,count(mylist, n)))