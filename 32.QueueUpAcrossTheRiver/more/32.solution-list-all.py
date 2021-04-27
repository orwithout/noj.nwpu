def Jump(s, y):
    k = 0
    if s == 0:
        k = y + 1
    else:
        k = 2 * Jump(s - 1, y)
    return k

#n,m=map(int,input().split(','))

for n in range(0,26):
    for m in range(0,26):
        print((m+1)*2**n,Jump(n, m))
