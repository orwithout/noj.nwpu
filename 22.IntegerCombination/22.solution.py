"""
def intcomb():
    n=eval(input())
    m=eval(input())
    n=int(n)
    m=int(m)
    
    u=0
    v=0
    if n>9 or n<0:
        print("error")
        return
    elif n!=0:
        if m>0:
            for i in range(1,m+1):
                v=v+n*10**(i-1)
                #print(v)
                u=u+v
        elif m<0:
            for i in range(1,-1*m+1):
                v=v+n*10**(-1*i)
                #print(v)
                u=u+v
    print(u)

#def intcomb2():

intcomb()

'''
for i in range(1,100):
    intcomb()
'''
"""
a=input()
n=int(input())
sum=0
for i in range(1,n+1):
    b=a*i
    sum+=int(b)
print(sum)
