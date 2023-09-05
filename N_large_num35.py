# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:37:19 2023

@author: srushti
"""

list1 = [4,7,56,76,34,42]  
 
list1.sort()  
print("Sorted List:")  
print(list1)  
n=int(input("Enter Number You Want:"))
print("Second largest element is:", list1[-n])