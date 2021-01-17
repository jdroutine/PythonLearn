def no_of_copies(text, copies):
    if len(text) >= 2:
        return text[0:2] * copies
    else:
        return text * copies

text = input('Enter the character string: ')
copies = int(input('How many copied you want  to print?: '))

print(no_of_copies(text, copies))