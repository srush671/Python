# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:40:29 2023

@author: srushti
"""

min=int(input("Enter Number:"))
max=int(input("Enter Number:"))




for n in range(min,max+1):
    sum=0
    temp=n
    while temp>0:
       rem=temp%10
       sum=sum+(rem*rem*rem)
       temp=temp//10
       if(n==sum):
         print(n)