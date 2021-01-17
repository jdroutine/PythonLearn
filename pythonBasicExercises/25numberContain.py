def group_of_values(values, number):
    for element in values:
        if number == element:
            return True
    return False

values = [1, 5, 8, 3, 3]

number = int(input('Enter the number to check is it in group of numbers 1,5,8,3,3: '))

print(group_of_values(values, number))