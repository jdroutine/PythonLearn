"""
Created on Thu Jul 23 14:49:21 2020

@author: jd.devroutine
"""


def string_input():
    sentence = input("Wprowadź ciąg znaków zawierakjący kilka wyrazów: ")
    return sentence


def backwards_order(result):
    result2 = result.split()
    result2.reverse()


sentence = string_input()
print(backwards_order(sentence))
