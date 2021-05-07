def GenerateDictionary(m,n):
    d={}
    for i in range(0,min(len(m),len(n))):
        d[m[i]] = n[i]
    return d

m=list(input().split())
n=list(input().split())
print(GenerateDictionary(m,n))
