def factorialFactors(n,a):
    m=0
    for i in range(1,n):
        m += n//(a**i)
        if a**(i+1)>n:
            return m

n=int(input())
if 1<=n<=2**109:
    print(factorialFactors(n,5))
else:
    print("error")
