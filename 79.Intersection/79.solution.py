
sm = set(input().split())
sn = set(input().split())
smn = sm.intersection(sn)

t=[]
rst =""
for i in smn:
    rst = rst + str(i) + ' '
print(rst[:-1])
