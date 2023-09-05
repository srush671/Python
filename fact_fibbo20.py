# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:21:19 2023

@author: srushti
"""

N=int(input("Enter number"))

print("Fibonacci")
n1=0
n2=1
count=0

while count<N:
    print(n1)
    next=n1+n2
    n1=n2
    n2=next
    count=count+1

print("Factorial")
fact=1
for i in range(1,N+1):
    fact=fact*i
    print(fact)
