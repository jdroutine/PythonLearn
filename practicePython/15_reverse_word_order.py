"""
Created on Thu Jul 23 14:49:21 2020

@author: jd.devroutine
"""


def string_input():
    sentence = input("Wprowadź ciąg znaków zawierający kilka wyrazów: ")
    return sentence


def backwards_order(result):
    result2 = result.split()
    return " ".join(reversed(result2))


sentence = string_input()
print("Odwrócony ciąg znaków to:", backwards_order(sentence))
