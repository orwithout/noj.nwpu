def maxNumberOfFrogs(Y,S):
    #Y为河中荷叶数、S为河中石墩数
    #首个石墩最多可以叠青蛙数为：(Y+S-1) + (Y+S-2) + … + (Y+1) +  Y + 1
    #次个石墩最多可以叠青蛙数为：          (Y+S-2) + … + (Y+1) +  Y + 1
    #最末一个石墩可以叠青蛙数为：                                  Y + 1
    sf=0
    for i in range(1,S+1):
        sf += (Y+i-1+Y)/2*i + 1
    #石墩上叠加的数量加上荷叶数量加上岸上的一只，为总数：
    return int(sf+Y+1)


m,n=map(int,input().split(','))
while 0<=m<=25 and 0<=n<=25:
    print(maxNumberOfFrogs(m,n),(m+1)*2**n)
    m,n=map(int,input().split(','))
