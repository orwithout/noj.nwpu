a=int(input())
er1=bin(a)
er2=str(er1)[2:]
ba2=oct(a)
ba1=str(ba2)[2:]
shi2=hex(a)
shi1=str(shi2)[2:]
shi3=str(shi2).upper()
l=[er2,ba1,ba2,shi1,shi2]
for i in l:
    print(i,end=',')
print(shi3)
