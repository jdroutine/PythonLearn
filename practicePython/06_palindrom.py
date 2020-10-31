"""
Created on Fri Jul 10 18:44:48 2020

@author: jd.devroutine
"""
word = input("Podaj słowo aby sprawdzić czy jest palindromem >>> ")
rvsWord = word[::-1]

if word == rvsWord:
    print("Słowo", word,"jest palindromem.")
else:
    print("Słowo", word,"nie jest palindromem.")

