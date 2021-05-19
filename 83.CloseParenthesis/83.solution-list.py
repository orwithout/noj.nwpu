
def isClose1(ps):
    while len(ps) > 0:
        if ps[0] == '(' or ps[0] == '[' or ps[0] == '{':
            t = len(ps)
            for i in range(1,t):
                if (ps[0] == '(' and ps[i] == ')') or (ps[0] == '[' and ps[i] == ']') or (ps[0] == '{' and ps[i] == '}'):
                    ps = ps[1:i] + ps[i+1:]
                    #print(ps)
                    break
            if len(ps) == t:
                break
        else:
            return False
    if len(ps) == 0:
        return True
    else:
        return False


def isClose2(ps,psd):
    if len(ps) == 0 or ps[0] not in psd:
        return False
    pst = ps
    for i in range(1,len(ps)):
        if ps[i] == psd[ps[0]]:
            pst = ps[1:i] + ps[i+1:]
            if len(pst) > 0:
                return True and isClose2(pst,psd)
            else:
                return True
    if len(pst) == len(ps):
        return False


class pstr:
    def __init__(self,psd):
        self.psd = psd
    def isClose(self,ps):
        if len(ps) == 0 or ps[0] not in self.psd:
            return False
        pst = ps
        for i in range(1,len(ps)):
            if ps[i] == self.psd[ps[0]]:
                pst = ps[1:i] + ps[i+1:]
                if len(pst) > 0:
                    return True and self.isClose(pst)
                else:
                    return True
        if len(pst) == len(ps):
            return False



psd = {'(':')','[':']','{':'}'}
cps = pstr(psd)
ps = input()
while ps != '':
    print(cps.isClose(ps),isClose1(ps),isClose2(ps,psd))
    ps = input()

