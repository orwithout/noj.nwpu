
def RomanNum2Num(rs,rn,E):
    if len(rs) == 0:
        return E
    for i in range(min(len(rs),4),0,-1):
        if rs[:i] in rn:
            return RomanNum2Num(rs[i:],rn,E+rn[rs[:i]])

rs = input()
rn = {'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9}
rn.update({'X':10,'XX':20,'XXX':30,'XL':40,'L':50,'LX':60,'LXX':70,'LXXX':80,'XC':90})
rn.update({'C':100,'CC':200,'CCC':300,'CD':400,'D':500,'DC':600,'DCC':700,'DCCC':800,'CM':900})
rn.update({'M':1000,'MM':2000,'MMM':3000})

print(RomanNum2Num(rs,rn,0))
