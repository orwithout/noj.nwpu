# 数字        ：0  1  2  3  4  5  6  7  8  9
# 需要火柴根数：6  2  5  5  4  5  6  3  7  6
# 可成数字根数：2 3 4 5 5 5 6 6 6 7
# n根可组成数字个数k：n//7 <= k <= n//2

def StickNumbers(n):
    k=[]
    if n<2:
        return k
    for i0 in range(0,n//6+1):
        t123456789 = n - i0*6
        if t123456789==0:
            k.append([n]+[0]*i0)
            break
        for i1 in range(0,t123456789//2+1):
            t23456789 = t123456789 - i1*2
            if t23456789==0:
                k.append([n]+[0]*i0 + [1]*i1)
                break
            for i2 in range(0,t23456789//5+1):
                t3456789= t23456789 - i2*5
                if t3456789==0:
                    k.append([n]+[0]*i0 + [1]*i1 + [2]*i2)
                    break
                for i3 in range(0,t3456789//5+1):
                    t456789= t3456789 - i3*5
                    if t456789==0:
                        k.append([n]+[0]*i0 + [1]*i1 + [2]*i2 + [3]*i3)
                        break
                    for i4 in range(0,t456789//4+1):
                        t56789= t456789 - i4*4
                        if t56789==0:
                            k.append([n]+[0]*i0 + [1]*i1 + [2]*i2 + [3]*i3 + [4]*i4)
                            break
                        for i5 in range(0,t56789//5+1):
                            t6789= t56789 - i5*5
                            if t6789==0:
                                k.append([n]+[0]*i0 + [1]*i1 + [2]*i2 + [3]*i3 + [4]*i4 + [5]*i5)
                                break
                            for i6 in range(0,t6789//6+1):
                                t789= t6789 - i6*6
                                if t789==0:
                                    k.append([n]+[0]*i0 + [1]*i1 + [2]*i2 + [3]*i3 + [4]*i4 + [5]*i5 + [6]*i6)
                                    break
                                for i7 in range(0,t789//3+1):
                                    t89= t789 - i7*3
                                    if t89==0:
                                        k.append([n]+[0]*i0 + [1]*i1 + [2]*i2 + [3]*i3 + [4]*i4 + [5]*i5 + [6]*i6 + [7]*i7)
                                        break
                                    for i8 in range(0,t89//7+1):
                                        t9= t89 - i8*7
                                        if t9==0:
                                            k.append([n]+[0]*i0 + [1]*i1 + [2]*i2 + [3]*i3 + [4]*i4 + [5]*i5 + [6]*i6 + [7]*i7 + [8]*i8)
                                            break
                                        for i9 in range(0,t9//6+1):
                                            ta = t9 - i9*6
                                            if ta==0:
                                                k.append([n]+[0]*i0 + [1]*i1 + [2]*i2 + [3]*i3 + [4]*i4 + [5]*i5 + [6]*i6 + [7]*i7 + [8]*i8 + [9]*i9)
                                                break
    return k


L = [6,2,5,5,4,5,6,3,7,6]
p = 0
nn= []


def NumbersPermutations(nn):
    for i in range(


def StickNumbers2(K,n,L,p,P):    # n > 0
    if n==0:
        return NumbersPermutations(K)
    elif p > P:
        return 0
    else:
        E = 0
        for m in range(0,n+1,L[p]):
            return E += StickNumbers2(K+[m//L[p]],n-m,L,p+1,P)
        return E



for i in range(0,101):
    k = StickNumbers(i)
    print("____________________________________________")
    #print(k)
    #if len(k) <= 0:
        #print("len-k",len(k),k)
    for j in range(0,len(k)):
        print(j)
        print(k[j])

"""
n = int((input()))
while n > 0:
    print(InterestRateGrowth(1.01,n))
    print(1.01**n)
    n = int((input()))
"""
