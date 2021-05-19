import copy
class numsSet:
    def subsets(self,nn):
        if len(nn) == 0:
            return [[]]
        t = self.subsets(nn[1:])
        sbls = copy.deepcopy(t)
        for i in t:
            sbls.append([nn[0]] + i)
        return sbls

aa = numsSet()
nn = list(map(int,input().split()))
nn.sort()
print(aa.subsets(nn))
