a=eval(input())
b=eval(input())
c=(a*a+b*b)**0.5#两直角边
d=(max(a,b)*max(a,b)-min(a,b)*min(a,b))**0.5#一斜边一直角边
m=c!=int(c)
n=d!=int(d)
o=a-b<c<a+b
p=a-b<d<a+b

if (m and n):
    print("non")
elif o and not m:
    print("c")
elif p and not n:
    if d>min(a,b):
        print("b")
    else:
        print("a")
