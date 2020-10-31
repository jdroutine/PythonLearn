"""
Created on Sun Jul 19 12:46:39 2020

@author: jd.devroutine
"""


def list_ends(list_a):
    return [list_a[0], list_a[-1]]


list_a = [5, 10, 15, 20, 25]
b = list_ends(list_a)

print(b)
