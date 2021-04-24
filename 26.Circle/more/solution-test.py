
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
x3=eval(input())
y3=eval(input())
def jieeryuanfangcheng(a,b,c,d,e,f):
    di=a*e-b*d
    if di==0:
        print("error")
    else:
        x=(c*e-b*f)/di
        y=(a*f-c*d)/di
    return x,y
a=2*x1-2*x2
b=2*y1-2*y2
c=x1*x1-x2*x2+y1*y1-y2*y2
d=2*x1-2*x3
e=2*y1-2*y3
f=x1*x1-x3*x3+y1*y1-y3*y3
x0,y0=jieeryuanfangcheng(a,b,c,d,e,f)
r=((x1-x0)**2+(y1-y0)**2)**0.5
print(round(r,3),round(x0,3),round(y0,3),sep=',')
