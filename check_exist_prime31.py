# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:01:40 2023

@author: srushti
"""

tuple = (1,5,8,7,2,3,4,6,9,10)
n=int(input("Enter Number You Want To Check"))
print(n in tuple)
flag = 0
for i in range(2,n):
  if n%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")
