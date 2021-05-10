def elementsMutiplication(m):
    E = 1
    for i in m:
        E *= i
    return E

m = map(int,input().split())
print(elementsMutiplication(m))
