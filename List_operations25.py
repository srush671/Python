# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:59:35 2023

@author: srushti
"""

List1=[1,2,3,5,6,7]
print("Length of list:")
print(len(List1))

List1.append(10)
print("List After Appending New Value:")
print(List1)

List1.extend([12,15])
print("List After Extending New Values:")
print(List1)

List1[1:5]
print("List After Extending New Values:")
print(List1)

List1=[1,2,3,5,6,7]
r=1
for i in List1:
    r=r*i
print("Multiplication of List Elements")
print(r)

List1=[1,2,3,5,6,7]
print("multiply lists:")
print(List1*2)



