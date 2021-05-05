def MaxDivisor(d):
    a = d[0]
    b = d[1]
    while a%b != 0:
        tmp=a%b
        a = b
        b = tmp
    return b


def fun(a, b, acb):
    x = 1
    y = 0
    while True:
        y = (acb-x*a)//b
        if acb == a*x+b*y:
            return x, y
        x += 1


def Euclid(a,b):
    a,b=(min(a,b),max(a,b))
    t = b%a
    if t==0:
        return a
    return Euclid(t,a)


def ExEuclid(a,b,d):
    x=0
    y=0
    t =a*x + b*y
    while t != d:
        if t > d:
            y -=1
        else:
            x +=1
        t =a*x + b*y
    return x,y

for a in range(50,100):
    for b in range(1,100):
        print(a,b,Euclid(a,b),ExEuclid(a,b,Euclid(a,b)),fun(a, b, MaxDivisor([a,b])))
        
