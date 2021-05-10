def unionSet(sm,sn):
    smn = sm.union(sn)
    lst = list(smn)
    lst.sort()
    rst =""
    for i in lst:
        rst = rst + str(i) + ' '
    return rst[:-1]

sm = set(input().split())
sn = set(input().split())
print(unionSet(sm,sn))
