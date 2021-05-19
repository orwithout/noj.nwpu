
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


cps = pstr({'(':')','[':']','{':'}'})
ps = input()
while ps != '':
    print(cps.isClose(ps))
    ps = input()
