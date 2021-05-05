"""
第一个盘子有多少种分法,加上分配了第一个盘子后，
下一个盘子的分法，下一个盘子得苹果数不小于第一个盘子苹果数，
这样即使得每个盘子分得的苹果数按小到大顺序排列，分法不会被重复计算。
第一个盘子分配分法有最少1个到最多m个，后面的盘子即都分配为0，
因此第一个盘子分法不从0个分配开始计数
"""
def DivideApple(m,n,k):
    if m == 0:
        return 1
    if n == 0:
        return 0
    E=0
    for i in range(k,m+1):
        E += DivideApple(m-i,n-1,i)
    return E

m,n = map(int,input().split())
print(DivideApple(m,n,1))
