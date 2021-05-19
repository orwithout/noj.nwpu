
class numList:
    def zeroSum3s(self,nn):
        rtn = list()
        t = len(nn)
        if len(nn)<3:
            return rtn
        for i in range(0,t-2):
            for j in range(i+1,t-1):
                for k in range(j+1,t):
                    if nn[i] + nn[j] + nn[k] == 0:
                        rtn.append([nn[i],nn[j],nn[k]])
        return rtn

aa = numList()
nn = list(map(int,input().split()))
print(aa.zeroSum3s(nn))
