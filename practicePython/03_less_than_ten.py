a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []

print("\nLiczby w tabeli \"a\" < 5:")

print([elements for elements in a if elements < 5])

num = int(input("Podaj liczbę: "))

for elements in a:
    if elements < num:
        c.append(elements)

print("\nLiczby w tabeli \"a\" mniejsze od", num, "to: ", c)
