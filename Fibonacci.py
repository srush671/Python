# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:05:06 2023

@author: srushti
"""

range=int(input("Enter Range:"))

n1=0
n2=1
count=0

while count<range:
    print(n1)
    next=n1+n2
    n1=n2
    n2=next
    count=count+1
    
    