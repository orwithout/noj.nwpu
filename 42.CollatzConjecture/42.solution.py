
def CallotzSeq(n):
    if n==1:
        return "1"
    elif n%2==0:
        return str(n)+"," + CallotzSeq(int(n/2))
    else:
        return str(n)+"," + CallotzSeq(3*n+1)

n = int(input())
if n>0:
    print(CallotzSeq(n))
