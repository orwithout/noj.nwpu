# 数字        ：0  1  2  3  4  5  6  7  8  9
# 需要火柴根数：6  2  5  5  4  5  6  3  7  6
# 可成数字根数：2 3 4 5 5 5 6 6 6 7
# n根可组成数字个数k：n//7 <= k <= n//2




def stick_number(num):
    # 函数返回两位数字num需要的火柴个数
    # 记录下数字0~9需要的火柴个数
    stick_num = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    result = 0
    if num < 10:
        result = stick_num[num]
    elif 10 <= num < 100:
        # 返回个位和十位的火柴个数
        result = stick_num[num%10] + stick_num[num//10]
    elif 100 <= num < 1000:
        result = stick_num[num%10] + stick_num[(num//10)%10] + stick_num[num//100]
    else:
        result = stick_num[num%10] + stick_num[(num//10)%10] + stick_num[num//100%10] + stick_num[num//1000]
    return result


def stick_eqution(n):
    count = 0
    if n <= 4:
        return count
    else:
        n -= 4 # 减去+和=用去的4根火柴
        for num1 in range(1000):
            for num2 in range(1000):
                if stick_number(num1) + stick_number(num2) + stick_number(num1 + num2) == n:
                    count += 1
    return count







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


L = [6,2,5,5,4,5,6,3,7,6]
nn= ""
for i in range(4,26):
    k = howManyNumbersStr(L,nn,i-4)
    k2 = stick_eqution(i)
    print("----n,k,k2:",i,k,k2)


"""
n = int((input()))
while n > 0:
    print(InterestRateGrowth(1.01,n))
    print(1.01**n)
    n = int((input()))
"""
