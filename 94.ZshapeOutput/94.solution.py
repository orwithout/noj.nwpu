
n=int(input())
nn = list()
for i in range(n):
    nn.append(list(input().split(' ')))
tt = nn[0]
for i in range(1,n-1):
    tt = tt + [nn[i][n-1-i]]
tt = tt + nn[n-1]
print(' '.join(tt))
