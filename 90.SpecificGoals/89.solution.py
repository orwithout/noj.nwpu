
class Circle:
    def __init__(self,r):
        self.r = r
        self.pi = 3.14
    def area(self):
        return self.r * self.r * self.pi
    def perimeter(self):
        return self.r * 2 * self.pi

r = eval(input())
aa = Circle(r)
print(aa.area(),aa.perimeter())
