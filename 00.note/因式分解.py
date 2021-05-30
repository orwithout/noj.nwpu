def decomposePrimeFactors(n):
    nn = []
    for i in range(2,int(n**0.5)+1):
        if n%i ==0:
            nn += [i]
            n /= i
    if n > 1:
        nn += [int(n)]
    return nn



for n in range(1,100):
    print(decomposePrimeFactors(n))
        
