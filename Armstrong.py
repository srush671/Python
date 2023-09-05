# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:14:42 2023

@author: srushti
"""

n=int(input("Enter Any Number:"))
sum=0
temp=n
while temp>0:
    rem=temp%10
    sum=sum+(rem*rem*rem)
    temp=temp//10
if(n==sum):
  print(n,"is an Armstrong Number")
else:
  print(n,"is not an Armstrong Number")