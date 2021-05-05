

def Divide(m, n):
    if 0 == m or 1 == n:
       return 1
    elif n <= m:
        return Divide(m, n-1) + Divide(m-n, n)
    else:
        return Divide(m, m)


def DivideApple(m,n,k):
    if m == 0:
        return 1
    if n == 0:
        return 0
    E=0
    for i in range(k,m+1):
        E += DivideApple(m-i,n-1,i)
    return E


for m in range(1,100):
    for n in range(1,100):
        #m,n = map(int,input().split())
        print(m,n,DivideApple(m,n,1),Divide(m,n))
