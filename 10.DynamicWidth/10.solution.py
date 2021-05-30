m=int(input())
n=int(input())
m=str(bin(m))[2:]
k=len(m)
if n>k:
    m=m.zfill(n)
    print(m)
else:
    print(m)
