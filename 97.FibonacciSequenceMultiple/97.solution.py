def fiboSeqMultiple(n,k):    # k !=0
    fin,fi,fii = 0,0,1
    while n !=0:
        fin,fi,fii = fin+1,fii,fii+fi
        n = n-1 if fi % k == 0 else n
    return fin

n,k = map(int,input().split())
print(fiboSeqMultiple(n,k))
