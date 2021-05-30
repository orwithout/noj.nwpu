n=eval(input())
def feibonaqi(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return feibonaqi(n-1)+feibonaqi(n-2)
print(feibonaqi(n))

