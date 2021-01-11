def even_checker(n):
    if n % 2 == 0:
        print('Number {} is even!'.format(n))
    else:
        print('Number {} is odd!'.format(n))

number = int(input('Enter a number to check is it even or odd: '))

even_checker(number)