# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:58:17 2023

@author: srushti
"""

list1 = [1, 5, 57, 5, 3]

total = 1
for ele in range(0, len(list1)):
	total = total *list1[ele]

print("Multiplication of all elements in list: ", total)