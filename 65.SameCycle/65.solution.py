def isSameCycle(m,n):
    for i in range(0,len(m)):
        m = m[1:] + m[:1]
        if m == n:
            return True
    return False

m = input().split(' ')
n = input().split(' ')
print(isSameCycle(m,n))
