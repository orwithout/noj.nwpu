
class strList:
    def Reverse(self,ss):    #元组反向输出
        rtn = str()
        for i in ss:
            rtn = i + " " + rtn
        return rtn[:-1]

aa = strList()
ss = input().split()
print(aa.Reverse(ss))
