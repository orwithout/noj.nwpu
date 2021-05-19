
class Rectangle:
    def __init__(self,L,W):
        self.L = L
        self.W = W
    def area(self):    #计算矩形面积
        return self.L * self.W

L,W = map(int,input().split())
re = Rectangle(L,W)
print(re.area())
