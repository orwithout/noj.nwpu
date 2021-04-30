# 数字        ：0  1  2  3  4  5  6  7  8  9
# 需要火柴根数：6  2  5  5  4  5  6  3  7  6
# 可成数字根数：2 3 4 5 5 5 6 6 6 7

def howManyEquationsInStr(nn):
    ln=len(nn)
    hn=ln//2
    E = 0
    for i in range(1,hn+1):
        if nn[0]=="0" and i>1:
            continue
        for j in range(ln-1,i,-1):
            if (nn[i] == "0" and j-i>1) or (nn[j] == "0" and ln-j>1):
                continue
            if int(nn[:i]) + int(nn[i:j]) == int(nn[j:]):
                E += 1 
    return E


def howManyNumbersStr(L,nn,n):
    if n<0:
        return 0
    elif n==0:
        return howManyEquationsInStr(nn)
    else:
        E = 0
        for i in range(10):
            E += howManyNumbersStr(L,nn+str(i),n-L[i])
        return E


L = [6,2,5,5,4,5,6,3,7,6]    # L[i]=组成数字i需要的火柴数 (0<=i<=9)
nn= ""
n = int((input()))
if n <= 24:
    print(howManyNumbersStr(L,nn,n-4))


