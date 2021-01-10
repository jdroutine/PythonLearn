def sum(a, b, c):
    result = a + b + c
    if a == b and b == c:
        result = result * 3
    return result 

print(sum(1,2,3))
