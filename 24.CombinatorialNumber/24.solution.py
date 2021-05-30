#from scipy.special import comb, perm
def combnum():
    n=int(input())
    m=4
    if n>50 or n<0:
        return "error"
    return int(comb(n+m-1,m-1)-4*comb(n-10+m-1,m-1))



def combnum2():
    n=int(input())
    if n>50 or n<0:
        return "error"

    sum=0
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if a+b+c+d>n:
                        break
                    elif a+b+c+d==n:
                        #print(a,b,c,d)
                        sum+=1
                        break
                    else:
                        continue
    return sum


def combnum3():
    n=int(input())
    if n>50 or n<0:
        return "error"

    sum=0
    for a in range(0,10):
        for b in range(0,a):
            for c in range(0,b):
                for d in range(0,c):
                    if a+b+c+d>n:
                        break
                    elif a+b+c+d==n:
                        #print(a,b,c,d)
                        sum+=1
                        break
                    else:
                        continue
    return sum



#for i in range(1,100):
print(combnum2())
