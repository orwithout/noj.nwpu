
def ClosestFraction(n,a,b):
    ca = 1
    cb = n
    for ta in range(1,n):
        for tb in range(n,ta,-1):
            if ta * b >= tb *a:
                break
            elif ta * cb > tb * ca:
                ca = ta
                cb = tb
    return str(ca)+"/"+str(cb)

n,a,b=map(int,input().split(' '))
if 1<=a<b<=n<=1000:
    print(ClosestFraction(n,a,b))


