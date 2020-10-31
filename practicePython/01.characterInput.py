name = input("give me your name: ")
age = int(input("give me your age: "))
year = str((2020 - age)+100)

message = ("Hello " + name + "! In " + year + " you will have 100 years old!")

print(message)

number = int(input("give me a number: "))

for i in range(number):
    print(message)
