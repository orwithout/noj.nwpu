
m = input().split(',')
m.sort(key=lambda x:int(x[1:]))
" ".join(m)
print(" ".join(m))
