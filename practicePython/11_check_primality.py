"""
@author: jd.devroutine
"""


def prime_number():

    divisor = []

    for element in range(1, num+1):
        if (num % element == 0):
            divisor.append(element)
    print("Podana liczba dzieli się przez:", divisor)

    if (len(divisor) == 2):
        print("Jest to liczba pierwsza")

    elif (len(divisor) > 2):
        print("Jest to liczba złożona")

    else:
        print("Podana liczba nie jest ani pierwsza ani złożona")


num = int(input("Podaj numer aby sprawdzić czy jest liczbą pierwszą: "))
print()

prime_number()
