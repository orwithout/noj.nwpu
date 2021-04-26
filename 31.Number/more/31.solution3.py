def Number(n):
    m=0
    for a1 in range(0,n+1):
        for a2 in range(0,n+1):
            if (a1+a2)%2==0:
                for a3 in range(0,n+1):
                    e=(a1+a2+a3)
                    if (a2+a3)%3==0 and a2+a3>=3 and e%5==0 and m<e:
                        m=e
                        #print(a1,a2,a3)
    #print(3*n)
    return m+1


def Number2(n):
    m=0
    for a1 in range(0,n+1):
        for a2 in range(0,n+1):
            for a3 in range(0,n+1):
                e=(a1+a2+a3)
                if (a1+a2)%2==0 and (a2+a3)%3==0 and e%5==0 and m<e:
                    m=e
    return m



def Number3(n):
    max = (3 * n) // 5 * 5
    for t in range(max, -1, -5):
        for a2 in range(n, -1, -1):
            a3a = min(n, t - a2)
            for a3 in range(a3a, -1, -1):
                if (a2 + a3) % 3 == 0 and (t - a3) % 2 == 0 and (t - a2 - a3) <= n:
                    return t


for i in range(0,101):
    #n=int(input())
    if Number(i) != Number3(i):
        print("err")
    else:
        print("done")
        
        


