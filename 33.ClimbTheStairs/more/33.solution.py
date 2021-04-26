import math
def mathComb(n,m):
    return math.factorial(n)/(math.factorial(m)*math.factorial(n-m))

def ClimbTheStairs(n):
    e=0
    for i in range(0,n//3+1):
        for j in range(0,(n-3*i)//2+1):
            k=n-3*i-2*j
            m=i+j+k
            e += mathComb(m,i) * mathComb(m-i,j)
    return e

for i in range(0,101):
    n=int(input())
    if 0<n<100:
        print(ClimbTheStairs(n))


