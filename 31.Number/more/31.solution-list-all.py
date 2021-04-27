def numberGrid1(n):
    max = (3 * n) // 5 * 5
    for t in range(max, -1, -5):
        for a2 in range(n, -1, -1):
            a3a = min(n, t - a2)
            for a3 in range(a3a, -1, -1):
                if (a2 + a3) % 3 == 0 and (t - a3) % 2 == 0 and (t - a2 - a3) <= n:
                    print("  1",t-a2-a3,a2,a3,t)
                    return t

def numberGrid2(n):
    m=0
    e1=0
    e2=0
    e3=0
    for a1 in range(0,n+1):
        for a2 in range(0,n+1):
            for a3 in range(0,n+1):
                e=(a1+a2+a3)
                if (a1+a2)%2==0 and (a2+a3)%3==0 and e%5==0 and m<=e:
                    m=e
                    e1=a1
                    e2=a2
                    e3=a3
    print("  2",e1,e2,e3,m)
    return m


def numberGrid3(n):
    for a1 in range(n, 0, -1):
        for a2 in range(n, 0, -1):
            if (a1+a2)%2 != 0:
                continue
            for a3 in range(n, 0, -1):
                if  (a2+a3)%3 == 0 and (a1+a2+a3)%5 == 0:
                    max = a1+a2+a3
                    print("  3",a1,a2,a3,max)
                    return max


for i in range(0,101):
    #n=int(input())
    if 0<=i<=100:
        print("n =",i,":")
        numberGrid1(i)
        numberGrid2(i)
        numberGrid3(i)
