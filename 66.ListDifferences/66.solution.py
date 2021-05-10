def listDifferences(m,n):
    t = ""
    for i in m:
        if i not in n:
            t = t + ' ' + i
    for i in n:
        if i not in m:
            t = t + ' ' + i
    return t[1:]

m = input().split(' ')
n = input().split(' ')
print(listDifferences(m,n))
