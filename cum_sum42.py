# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:04:16 2023

@author: srushti
"""

list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
cum_list=[]   
y = 0  
for x in range(0,len(list)):  
    y=y+list[x]  
    cum_list.append(y)   
      
print(cum_list)   
