name = input("Enter Your Name And Second Name: ")
words = name.split()
words = list(reversed(words))
print(' '.join(words))