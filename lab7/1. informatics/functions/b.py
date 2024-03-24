def power(a, n):
    result = 1
    for i in range(n):
        result *= a
    return result


a, n = input().split()
a, n = int(a), int(n)
result = power(a, n)
print(result) 
