def simpleFraction(a,b):
    t = min(a,b)
    p = 2
    while p<=t:
        if a%p==0 and b%p==0:
            a /= p
            b /= p
            t = min(a,b)
            p = 2
        else:
            p +=1

    return a,b


for a in range(1,100):
    for b in range(100,a,-1):
        print(simpleFraction(a,b))
        
