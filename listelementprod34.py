# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:25:41 2023

@author: srushti
"""

def my_list(list) :
     
    product = 1
    for i in list:
         product = product * i
    return product
     

list1 = [11, 12, 4, 3]
print(list1)
print("product: ") 
print(my_list(list1))