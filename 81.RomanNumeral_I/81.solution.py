
def toRomanNum(n,rn):
    if len(rn) <= 1:
        return rn[0]*(n//10)
    t = n %10
    print(n,t)
    if 0<=t <= 3:
        return toRomanNum(n//10,rn[2:]) + rn[0]*t
    if t==4:
        return toRomanNum(n//10,rn[2:]) + rn[0] + rn[1]
    if 5<= t <9:
        return toRomanNum(n//10,rn[2:]) + rn[1] + rn[1]*(t%5)
    if t ==9:
        return toRomanNum(n//10,rn[2:]) + rn[0] + rn[2]
    return ""

n = eval(input())
rn = ['I','V','X','L','C','D','M']
print(toRomanNum(n,rn))
