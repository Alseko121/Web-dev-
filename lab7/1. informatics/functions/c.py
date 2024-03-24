def xor(x, y):
    if bool(x) != bool(y):
        return True
    else:
        return False


x, y = input().split()
x, y = bool(int(x)), bool(int(y))
result = xor(x, y)
print(int(result)) 

