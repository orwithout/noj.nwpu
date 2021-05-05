import math

def mathCatalan(n):
    return math.factorial(2*n)/(math.factorial(n+1)*math.factorial(n))


def algoCatalan(n):
    E = 1
    K = 1
    for k in range(2,n+1):
        E *= (n+k)
        K *= k
    return E/K

for n in range(50):
    print(mathCatalan(n),algoCatalan(n))
