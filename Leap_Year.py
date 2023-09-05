# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:34:55 2023

@author: srushti
"""

year=int(input("Enter Year:"))

if((year%400==0) or (year%100!=0) and (year%4==0)):
    print("Given Year is  Leap Year")
else:
    print("Given Year is Not Leap Year")