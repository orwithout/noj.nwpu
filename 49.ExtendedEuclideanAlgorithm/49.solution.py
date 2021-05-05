
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

a,b = map(int,input().split())
if a > 0 and b > 0:
    x,y = ExEuclid(a,b,Euclid(a,b))
    print(x,y)
