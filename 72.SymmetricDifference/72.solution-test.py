
def symmetricDifference(sm,sn):
    st =""
    for i in sm:
        if i not in sn:
            st = st + str(i) + ' '
    for i in sn:
        if i not in sm:
            st = st + str(i) + ' '
    return st[:-1]


sm = set(input().split())
sn = set(input().split())
print(symmetricDifference(sm,sn))
st = sm.symmetric_difference(sn)
s=""
for i in st:
    s = s + str(i) + ' '

print(s[:-1])

