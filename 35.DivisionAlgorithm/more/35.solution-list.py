
def DivisionAlgorithm(q,r):
    qs=str(q)
    q1=int(qs[0])
    q2=int(qs[1])
    q3=int(qs[2])
    q12=int(qs[:2])
    for d in range(10,100):
        if d*q1<=99 and d*q3>=100:
            f4 = (d*q3 + 1) % 10
            f12min = d*q1
            f12max = min(99,(d*q12+d)//10)
            for f12 in range(f12min,f12max):
                #f3min = max(0,d*q12 + 10 - f12*10)
                #f3max = min(10,d*q12 +  d - f12*10)
                #print(f3min,f3max)
                #for f3 in range(f3min,f3max):
                for f3 in range(0,10):
                    f=f12*100+f3*10+f4
                    if f-d*q==1:
                        #print(q,r,d,f12,f3min,f3max,f3,"x",)
                        print(q,":",d,f,f-d*q,q1*d,q3*d,f12*10+f3-q12*d,f12,f3,f4)

q=int(input())
while 100<=q<=999:
    print(q)
    DivisionAlgorithm(q,1)
    q+=1
    #q=int(input())
