
def decomposeFactors(a,q):
    if a==1:
        return 1
    if q==1:
        return 0
    E=0
    for i in range(q,0,-1):    # 取第一个乘的种数加上取了第一个乘后、取下一个乘的种数
        if a%i==0:
            E += decomposeFactors(a/i,i)
    return E


n = int(input())
if n > 0:
    print(decomposeFactors(n,n))
