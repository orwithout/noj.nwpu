
def factorialFactors(n,a):
    m=0
    for i in range(1,n):
        m += n//(a**i)
        if a**(i+1)>n:
            return m



import math
def findZeros(n):
    temp = math.factorial(n)
    n = 0
    for i in range(len(str(temp))):
        if '0' == str(temp)[len(str(temp)) - i - 1]:
            n += 1
        else:
            return n



for i in range(1,100):
    n=int(input())
    if 1<=n<=2**109:
        print(factorialFactors(n,5))
        print(findZeros(n))
    else:
        print("error")
