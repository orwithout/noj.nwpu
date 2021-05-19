
class Circle:
    def __init__(self,r):
        self.r = r
        self.pi = 3.14
    def area(self):    #self.pi要放在后面,否则算出浮点数结尾不一样，不通过
        return self.r * self.r * self.pi
    def perimeter(self):
        return self.r * 2 * self.pi

r = eval(input())
aa = Circle(r)
print(aa.area(),aa.perimeter())
