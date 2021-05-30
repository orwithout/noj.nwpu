a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())
e=eval(input())
f=eval(input())
di=a*e-b*d
if di==0:
    print("error")
else:
    x=(c*e-b*f)/di
    y=(a*f-c*d)/di
    print("%.3f %.3f"%(x,y))
