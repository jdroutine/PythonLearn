"""
Created on Wed Jul  1 22:37:00 2020

@author: jd.devroutine
"""
import random

a = random.sample(range(10,30),10)
b = random.sample(range(10,30),12)
c = []

print("\nLista a:", a)
print("\nLista b:", b)
print()

for element in b:
    if element in a and element not in c:
        c.append(element)
        
print("Elementy wspólne:", c)