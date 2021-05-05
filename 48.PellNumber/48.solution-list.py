
def Pell(n):
    pell = [i for i in range(n+1)]
    pell[0] = 0
    pell[1] = 1
    for i in range(2, n+1):
        pell[i] = 2*pell[i-1] + pell[i-2]
    return pell[n]



def PellNum(n):
    if n<2:
        return n
    return 2*PellNum(n-1) + PellNum(n-2)

def PellNum2(n):
    p_2=0
    p_1=1
    p_n =n*p_1
    for i in range(2,n+1):
        p_n=2*p_1 + p_2
        p_2=p_1
        p_1=p_n
    return p_n


n=int(input())
if n>=0:
    print(Pell(n))
    print(PellNum2(n))
    print(PellNum(n))
