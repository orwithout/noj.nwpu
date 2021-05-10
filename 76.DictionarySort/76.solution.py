
sm=list()
while True:
    t = input()
    if t != "":
        tt = tuple(t.split())
        sm += [tt]
    else:
        break
sn = sm.copy()
sm.sort(key=lambda x:x[1])
sn.sort(key=lambda x:x[0],reverse=True)
print(sm)
print(sn)

