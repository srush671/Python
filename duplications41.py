# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:01:30 2023

@author: srushti
"""

list1 = [1, 2, 3, 4, 2, 7, 8, 8, 3];     
     
print("Duplicate elements in given array: ");    
    
for i in range(0, len(list1)):    
    for j in range(i+1, len(list1)):    
        if(list1[i] == list1[j]):    
            print(list1[j]);  