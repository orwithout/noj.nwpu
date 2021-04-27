
def DivisionAlgorithm(q,r):
    qs=str(q)
    q1=int(qs[0])
    q2=int(qs[1])
    q3=int(qs[2])
    q12=int(qs[:2])
    for d in range(10,100):    #满足d是个两位数
        if d*q1<=99 and d*q3>=100:    #满足商的第一位乘d是个两位数，和满足商的最后一位乘d是个三位数
            f4 = (d*q3 + 1) % 10    #被除数的第四位
            f12min = d*q1    #f12min和f12max用来限定被除数的第一第二(千和百)位的取值上下限
            f12max = min(100,(d*q12+d-1)//10+1)
            for f12 in range(f12min,f12max):
                #f3min = max(0,d*q12 + 10 - f12*10)
                #f3max = min(10,d*q12 +  d - f12*10)
                #print(f3min,f3max)
                #for f3 in range(f3min,f3max):
                for f3 in range(0,10):    #被除数的第三（十）位
                    f=f12*100+f3*10+f4
                    if f-d*q==1:
                        print(f,d)


q=int(input())
if 100<=q<=999:    #满足q是个三位数
    DivisionAlgorithm(q,1)
