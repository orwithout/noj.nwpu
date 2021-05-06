def delAllOddIndexValue(s):
    se = ""
    for i in range(0,len(s),2):
        se += s[i]
    return se

s=input()
while s!="":
    print(delAllOddIndexValue(s))
    s=input()

