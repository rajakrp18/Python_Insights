class Student1:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name, self.id)

    def file(self):
        f = open("avi.txt", "a")
        f.write("\nName=")
        f.write(self.name)
        f.write("\nid=")
        f.write(self.id)
        f.close()


class Student2(Student1):
    def __init__(self, name, id, project):
        super().__init__(name, id)
        self.project = project

    def display(self):
        print(self.project)
        super().display()

    def file(self):
        super().file()

        f = open("avi.txt", 'a')
        f.write('\nProject=')
        f.write(self.project)
        f.close()
        f = open("avi.txt", "r")
        print(f.read())
        f.close()


f = open('avi.txt', 'w')
f.write("")
f.close()
l = []
n = int(input("Enter the number of terms :"))
for i in range(0, n):
    x = input("Enter the value of Name :")
    y = input("Enter the value of ID :")
    z = input("Enter the value of Project :")
    s = Student2(x, y, z)
    # s.display()
    s.file()
    l.append(s)
    print("------------------")
