# https://blog.csdn.net/liyuanbhu/article/details/52891868

def calcCenterPoint():
    x1=eval(input())
    y1=eval(input())
    x2=eval(input())
    y2=eval(input())
    x3=eval(input())
    y3=eval(input())

    a = x1 - x2
    b = y1 - y2
    c = x1 - x3
    d = y1 - y3
    e = ((x1 * x1 - x2 * x2) + (y1 * y1 - y2 * y2)) / 2.0
    f = ((x1 * x1 - x3 * x3) + (y1 * y1 - y3 * y3)) / 2.0
    m = b * c
    n = a * d
    if m==n:
        return 0,"NULL","NULL","NULL"
    else:
        x0 = -(d * e - b * f) / (m-n)
        y0 = -(a * f - c * e) / (m-n)
        r=(((x1-x0)**2)+((y1-y0)**2))**0.5
        return 1,r,x0,y0


f,r,x0,y0=calcCenterPoint()
if f==0:
    print(r,x0,y0,sep=',')
else:
    print("%.3f,%.3f,%.3f" %(r,x0,y0))
