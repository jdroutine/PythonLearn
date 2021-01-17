def no_of_copies(text, copies):
    return text[0:2] * copies

text = input('Enter the character string: ')
copies = int(input('How many copied you want  to print?: '))

print(no_of_copies(text, copies))