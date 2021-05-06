def minMaxWordsIs(s):
    tt = s.split()
    w_min = tt[0]
    w_max = tt[0]
    for t in tt:
        if len(w_min) > len(t):
            w_min = t
        if len(w_max) < len(t):
            w_max = t
    return w_min,w_max


s=input()
if s!="":
    w_min,w_max = minMaxWordsIs(s)
    print(w_min)
    print(w_max)

