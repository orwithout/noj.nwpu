
def InvertedBinary2(n,nn):
    if n<2:
        return nn +str(n)
    return InvertedBinary2(n//2,nn +str(n%2))


n = int(input())
print(InvertedBinary2(n,""))

