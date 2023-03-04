class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def add(self, c):
        a = self.r+c.r
        b = self.i+c.i
        # print(a, b)
        c1 = complex(a, b)
        return c1

    def dis(self):
        print(f"({self.r}+{self.i}i)")
        print(f"({cc.r}+{cc.i}i)")


c = Complex(2, 3)
cc = Complex(3, 4)
c1 = c.add(cc)
c.dis()
print(c1)
