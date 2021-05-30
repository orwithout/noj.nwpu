a=float(input())
l=[round(a,6),round(a,2),round(a,8),'%.6e'%a]
for i in l:
    print(i,end='/')
print(format(a,','))
