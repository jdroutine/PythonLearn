import calendar

print('Calendar\n')
year = int(input('Enter The Year: '))
month = int(input('Enter The Number Of Month (format \"dd\"): '))
print()
print(calendar.month(year,month))