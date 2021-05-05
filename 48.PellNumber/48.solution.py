
def PellNum2(n):
    p_2=0
    p_1=1
    Pn =n*p_1
    for i in range(2,n+1):
        Pn=2*p_1 + p_2
        p_2=p_1
        p_1=Pn
    return Pn

n=int(input())
if n>=0:
    print(PellNum2(n))
