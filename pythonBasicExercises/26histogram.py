def histogram(symbol, a):
    for element in a:
        print(symbol * element)

symbol = input('Enter the symbol to draw histogram: ')
num = [1, 2, 3, 4, 5, 6]
histogram(symbol, num)
