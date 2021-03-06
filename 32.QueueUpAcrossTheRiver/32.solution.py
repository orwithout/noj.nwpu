"""
https://bbs.csdn.net/topics/30122110

设 q 为青蛙数，n、m为石墩、荷叶数
设F[n,m]表示河中间最多青蛙数，我们可以增加一个石墩，把原来F[n-1，m]个q移到新的第 n 个石墩上，
这时第 n 个石墩可以看成原来的右岸，这时此石墩上就有F[n-1，m]个 q 了，
而原先的右岸已有F[n-1，m]个 q 了，再将这个石墩上的移上去岸上共有2*F[n-1，m]个了。
由此可知：           F[n，m]=2*F[n-1，m]
                            =4*F[n-2，m]
                            ……
                            =(2^i)*F[n-i，m]
                            ……
                            =(2^n)*F[0，m]
当只有荷叶时,每个叶上只能有一个 q ,所以加上右岸可以跳上去的一个,共有m+1个 q ,
所以                F[n，m] = （m+1）*2^n

—————————————————————————————————————-
有上面我们可以在得到一个更简单的方法，大家应该明白荷叶是一个过渡作用，
有 m 个荷叶我们就可以渡过 m + 1 个 q 。
用G（n）表示石墩上的 q ，则可以得到：
                     G（n）=G（n-1）*2 + m+1
                     G（0）= m+1
我们就可以得到：　　 G（n）= ∑（m+1）*2^i (i=1,2,……,n-1)看清楚是到 n-1 不是到 n（自己想想为什么）
                           =（m+1）*(2^n-1)
加上最后荷叶上的 m+1 个 q ,所一总共有：
                            （m+1）*2^n
"""

n,m=map(int,input().split(','))
while 0<=m<=25 and 0<=n<=25:
    print((m+1)*2**n)
    n,m=map(int,input().split(','))
