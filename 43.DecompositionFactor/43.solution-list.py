
def dfs(a, m):
    if a == 1:
        return 1
    if m == 1:
        return 0
    if a % m == 0:
        return dfs(a,m-1) + dfs(a / m,m);  
    return dfs(a,m-1)


def decomposeFactors2(a,q):
    if a==1:
        return 1
    if q==1:
        return 0
    E=0
    for i in range(q,0,-1):
        if a%i==0:
            E += decomposeFactors2(a/i,i)
    return E



def howManyKinds(K,m,n,nn):
    if K==n:
        return 1
    elif K>n:
        return 0
    else:
        E=0
        for k in nn:
            if k>=m:
                E += howManyKinds(K*k,k,n,nn)
        return E


def decomposeFactors(n):
    nn = []
    mm = []
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            nn += [i]
            t = n/i
            if t != i:
                mm += [int(t)]
    return nn+mm[::-1]+[n]


#n = int(input())
for n in range(1,1000):
    nn = decomposeFactors(n)
    print(n,howManyKinds(1,1,n,nn),dfs(n,n),decomposeFactors2(n,n))
