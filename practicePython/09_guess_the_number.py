"""
@author: jd.devroutine
"""

import random

number = random.randint(1, 9)
user = 0
count = 0

print("Zgadnij numer")

while user != number and user != "exit":

    user = input("Podaj liczbę 1-9 lub wpisz exit aby zakończyć: ")
    if user == "exit":
        break
    count += 1
    user = int(user)

    if int(user) < number:
        print("Za mała!")

    elif int(user) > number:
        print("Za duża!")

    elif int(user) == number:
        print("Doskonale! Trafiłeś za", count, "razem!")
        break
