
n=list(map(int,input().split()))
tp = tuple([n[i]+n[::-1][i] for i in range(len(n))])
print(tp)
