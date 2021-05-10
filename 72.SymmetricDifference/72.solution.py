

sm = set(input().split())
sn = set(input().split())

smn = sm.symmetric_difference(sn)
t=[]
for i in smn:
    t += [i]
t.sort()
rst =""
for i in t:
    rst = rst + str(i) + ' '
    
print(rst[:-1])
