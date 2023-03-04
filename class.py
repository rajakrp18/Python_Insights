class Test1:
    v1 = 0

    def __init__(self):
        self.f = "20"

    def show1(self):
        print(f"{self.f}")
        return self.f

    def show2(cls):
        print(f"{cls.v1}")
        return cls.v1


t = Test1()
t.v1 = input("enter v1")

# f = Test1()
# f.v1 = int(input("enter v1"))
# f.show1()
# f.show2()

a = open("avi.txt", "w")
a.write(t.show2())
a.write(t.show1())
a.close()
a = open("avi.txt", "r")
print(a.read())
