
def RepeatingCharacter(ss):
    t = list(set(ss))
    t.sort(key=ss.index)
    rst=""
    for i in t:
        t=0
        for j in ss:
            if j==i:
                t +=1
        if t >1:
            rst = rst + i + " " + str(t) + "\n"
    return rst[:-1]


ss = list(input())
print(RepeatingCharacter(ss))
