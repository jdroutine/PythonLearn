def return_true(a, b):
    sum = a + b
    dif = abs(a-b)

    if a == b or sum == 5 or dif == 5:
        return True
    else:
        return False

print(return_true(3,2))
print(return_true(8,3))
print(return_true(2,2))
print(return_true(5,2))
