def EuclideanAlgo(a,b):
    a,b=(min(a,b),max(a,b))
    t = b%a
    if t==0:
        return a
    else:
        return EuclideanAlgo(t,a)


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





for a in range(1,100):
    for b in range(1,100):
        nn=str(a) + "/" + str(b) +"："
        for n in range(1,100):
            nn = nn + ClosestFraction(n,a,b) + ", "
        print(nn)

