
def algoCatalan(n):
    E = 1
    K = 1
    for k in range(2,n+1):
        E *= (n+k)
        K *= k
    return int(E/K)

n = int((input()))
if n >= 0:
    print(algoCatalan(n))
