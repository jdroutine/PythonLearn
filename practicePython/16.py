"""
@author:  jd.devroutine

"""
import random

elements = """"1234567890abcdefghijklmnoprstquwvxyz
!@#&*^%$ABCDEFGHIJKLMNOPRQUWVXYZ"""

easypass = ["123!", "qwerty", "admin", "321"]

menu = int(input("""Jak silne hasło wygenerować?
1- Silne
2- Średnie
3- Łatwe """))

if menu == 1:
    password = "".join(random.sample(elements, 10))
    print("\nTwoje hasło to:", password)

if menu == 2:
   password = "".join(random.sample(elements, 6))
   print("\nTwoje hasło to:", password)

if menu == 3:
   password = random.choice(easypass)
   print("\nTwoje hasło to:", password)
