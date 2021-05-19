class Circle:
    def __init__(self,r):
        self._r = r
    def area(self):
        return self._r*self._r*3.14
    def perimeter(self):
        return 2*self._r*3.14

class Circle2:
    def __init__(self,r):
        self.r = r
        self.pi = 3.14
    def area2(self):
        return self.r * self.r * self.pi
    def perimeter2(self):
        return self.r * 2 * self.pi

for i in range(100):
    r = float(i)
    c = Circle(r)
    aa = Circle2(r)
    print(r,c.area(), c.perimeter())
    print(r,aa.area2(),aa.perimeter2())
