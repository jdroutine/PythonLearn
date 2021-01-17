def vovel_or_not(text):
    if text in vovel:
        return 'this letter is a vovel'
    else:
        return 'this letter is not a vovel'

vovel = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']

letter = input('Enter the letter to check is it a vovel: ')

print(vovel_or_not(letter))