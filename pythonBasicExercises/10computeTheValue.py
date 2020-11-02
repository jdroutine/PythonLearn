num = int(input('Enter The Number To Compute The Value From Pattern n+nn+nnn: '))
#pattern = num + num * 11 + num * 111

#print('Value is:', pattern)

n1 = int( "%s" % num )
n2 = int( "%s%s" % (num,num) )
n3 = int( "%s%s%s" % (num, num, num) )
print (n1+n2+n3)