

def CallotzSeq(n):
    if n==1:
        return "1"
    elif n%2==0:
        return str(n)+"," + CallotzSeq(int(n/2))
    else:
        return str(n)+"," + CallotzSeq(3*n+1)

for n in range(1,100):
    nn = CallotzSeq(n)
    print(nn)
