#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:38:36 2020

@author: damian
"""  
num = int(input("Podaj dzielną: " ))
check = int(input("Podaj dzielnik: " ))
result = num / check

if result % 4 == 0:
    print("\nWynik {} jest wielokrotnością liczby 4".format(result))

elif result % 2 == 0:
    print("\nWynik {} jest liczbą parzystą.".format(result))

elif result % 2 !=0:
    print("\nWynik {} jest liczbą nieparzystą.".format(result))
    
if num % check == 0:
    print("Brak reszty z dzielenia.")
    
else:
    print("Występuje reszta z dzielenia.") 