def DictionaryAddition(sm,sn):
    smn=dict()
    for i in sm:
        if i in sn:
            smn[i] = sm[i]+sn[i]
        else:
            smn[i] = sm[i]
    for i in sn:
        if i not in sm:
            smn[i] = sn[i]
    return smn


sm=dict()
for i in input().split(","):
    t = i.split(":")
    sm[t[0]] = int(t[1])

sn=dict()
for i in input().split(","):
    t = i.split(":")
    sn[t[0]] = int(t[1])

print(DictionaryAddition(sm,sn))
