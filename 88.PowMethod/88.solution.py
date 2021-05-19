
class twoInts:
    def intPow(self,x,n):
        rtn = 1
        for i in range(abs(n)):
            rtn = rtn * x
        if n < 0:
            if x == 0:
                return "0 cannot be raised to a negative power"
            else:
                return 1 / rtn
        else:
            return rtn

aa = twoInts()
x,n = map(int,input().split())
print(aa.intPow(x,n))
