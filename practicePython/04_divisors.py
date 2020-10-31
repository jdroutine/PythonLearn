#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:13:24 2020

@author: jd.devroutine
"""

num = int(input("Podaj liczbę aby sprawdzić jej dzielniki: "))
divisor = []

for element in range(1,num+1):
    if num % element == 0:
        divisor.append(element)
        
print(divisor)
