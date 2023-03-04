# # for loop
# list1 = [["harry", 10], ["larry", 20], ["carry", 30], ["garry", 40]]
#
# for total,lollypop in list1: #this is called the unpacking of list of list
#     print("this person",total,"have eaten",lollypop,"lollypops")
#
# # while loop
# i = 1
#
# while i <= 45:
#     print(i)
#     i=i+1

# Operators In Pythons
# Arithmetic Operators
# Assignment Operators
# Comparison Operators
# Logical Operators
# Identity Operators
# Membership Operators
# Bitwise Operators

# # Arithmetic Operators
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6)
# print("5 ** 3 is ", 5**3)
# print("5 % 5 is ", 5%5)
# print("15 // 6 is ", 15//6)
# print("15 % 6 is ", 15%6)
# # Assignment Operators
# # print("Assignment Operators")
# # x = 5
# # print(x)
# # x %=7 # x = x%7
# # print(x)
#
# # Comparison Operators
# i = 5
#
#
# # Logical Operators
# a = True
# b = False
#
# # Identity Operators
# # print(5 is not 5)
#
# # Membership Operators
# list = [3, 3,2, 2,39, 33, 35,32]
# # print(324 not in list)
#
# # Bitwise Operators
# # 0 - 00
# # 1 - 01
# # 2 - 10
# # 3 - 11
#
# print(0 & 2)
# print(0 | 3)
#
# # functions in python
# a=10
# b=11
# c=sum((a,b))
# print(c)

# # file concepts
# f = open("raj.txt", "rt")
# # content = f.read()
# # print(content)
#
# # for lines in f:
# #     print(lines)
#
# # print(f.readline())
# # print(f.readline())
# print(f.readlines())
# f.close()
# a = 9
# b = 8
# c = sum((a, b)) # built in function

def function1(a, b):
    print("Hello you are in function 1", a+b)

def function2(a, b):
    """This is a function which will calculate average of two numbers
    this function doesnt work for three numbers"""
    average = (a+b)/2
    # print(average)
    return average

# v = function2(5, 7)
# print(v)
print(function2.__doc__)
