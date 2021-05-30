
aa = input().split(' ')
nn = list(map(int,input().split(' ')))
tt = list()
for i in range(min(nn),max(nn)+1):
    for j in range(len(nn)):
        if nn[j] == i:
            tt = tt + [aa[j]]
print(' '.join(tt))
