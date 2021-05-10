sm = dict()
for i in input().split(","):
    t = i.split(":")
    sm[t[0]] = eval(t[1])
tmax=sm[list(sm.keys())[0]]
tmin=tmax
for i in sm:
    if sm[i] > tmax:
        tmax = sm[i]
    if sm[i] < tmin:
        tmin = sm[i]
        
print(tmax,tmin)
