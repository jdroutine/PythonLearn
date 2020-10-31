"""
Created on Wed Jul 15 20:35:23 2020

@author: jd.devroutine
"""
import random

a = random.sample(range(10, 30), 10)
b = random.sample(range(10, 30), 12)
c = []

c = [number for number in b if number in a and number not in c]

print(c)
