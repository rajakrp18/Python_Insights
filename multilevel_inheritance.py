# example of multilevel inheritance
class Test1:
    def _init_(self, name, id):
        self.name = name
        self.id = id
        print(self.name)
        print(self.id)


class Test2(Test1):
    def _init_(self, name, id, dept):
        super()._init_(name, id)
        self.dept = dept
        print(self.dept)


class Test3(Test2):
    def _init_(self, name, id, dept, sal):
        super()._init_(name, id, dept)
        self.sal = sal
        print(self.sal)


t = Test3("Raj", 1, "MCA", 120000)
