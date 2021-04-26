def Number(n):
    m=0
    
    for i in range(0,n//2+1):
        for j in range(0,n//3+1):
            
            if (a1+a2)%2==0:
                for a3 in range(0,n+1):
                    e=(a1+a2+a3)
                    if (a2+a3)%3==0 and e%5==0 and m<e:
                        m=e
                        #print(a1,a2,a3)
    return m

#for i in range(1,100):
n=int(input())
if 0<=n<=100:
    print(Number(n))
else:
    print("error")

