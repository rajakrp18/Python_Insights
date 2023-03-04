class Employee:
    def _init_(self):
        self.name = ""
        self.sal = 0

    def getName(self, name):
        self.name = name

    def showName(self):
        return self.name

    def getSal(self, sal):
        self.sal = sal

    def showSal(self):
        return self.sal


def inp():
    for i in range(0, 5):
        name = input("Enter name:")
        sal = int(input("Enter salary:"))
        e = Employee()
        e.getName(name)
        e.getSal(sal)
        l.append(e)


def sortSal():
    for i in range(0, 5):
        min = l[i].showSal()
        for j in range(i+1, 5):
            max = l[j].showSal()
            if min > max:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp


def display():
    for i in l:
        print(i.showName(), "\t ", i.showSal())


l = []
inp()
sortSal()
display()
