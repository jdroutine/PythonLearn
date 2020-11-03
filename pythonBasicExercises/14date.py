from datetime import date

d1 = date(2014, 7, 2)
d2 = date(2014, 7, 11)


delta = d2 - d1

print('The time between dates is:', delta.days, 'days.')