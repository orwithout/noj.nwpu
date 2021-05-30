
import math

x=eval(input())
y=eval(input())
r=(x*x+y*y)**0.5

if x==0:
    if y>0:
        o=math.pi*1/2
    elif y==0:
        o=0
    elif y<0:
        o=math.pi*3/2      
elif x<0:
    o=math.pi + math.atan(y/x)
elif y<0:
    o=math.pi*2 + math.atan(y/x)
else:
    o=math.atan(y/x)

print("%.4f,%.4f" %(r,o))
