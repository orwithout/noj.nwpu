def InvertedBinary(n):
    st = str('{:b}'.format(n))
    return st[::-1]

def InvertedBinary2(n,nn):
    if n<2:
        return nn +str(n)
    return InvertedBinary2(n//2,nn +str(n%2))

for n in range(-100,100):
    print(n,InvertedBinary2(n,""),InvertedBinary(n))
    
