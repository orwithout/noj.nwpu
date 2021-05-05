def nnSum(n,v):
    E=0
    if n <=0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(0,v+1):
            E += nnSum(n-1,v-i)
        return E
    


n,v=map(int,input().split())
print(nnSum(n,v))
