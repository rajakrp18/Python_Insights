# import playsound
# from playsound import playsound
# playsound('C:\\Users\\Raj Poddar\\PycharmProjects\\pythonProject\\play.mp3')
# import os
# print(os.listdir())
# some string functions
# name1='raj is a good boy boy'
# print(name1[0:5])
# name='Raj Poddar'
# print(len(name))
# print(name[0:10])
# print(name.endswith('ar')) #returns true value
# print(name.count('a'))
# print(name.capitalize())
# print(name.find('ar'))
# making a template for writing letter
# letter = '''Dear <|Name|>
# You are selected!
#
# Date: <|Date|>
# '''
# name=input("Enter your name\n")
# date=input("Enter date\n")
# letter = letter.replace('<|Name|>',name)
# letter = letter.replace('<|Date|>',date)
# print(letter)
# find and replace function
# st="This is a string with double   spaces"
# print(len(st))
# doublespaces=st.find("  ")
# print(doublespaces)
# st=st.replace("  ","")
# print(st)

# lists
friends = ['Apple', 'Akash', 'Rohan', 7,6.9, False] #<-- this is a list that is enclosedm in square barckets
print(friends)
a = [1, 2, 4, 56, 6]
print(a)
print(a[0]+a[1]+a[2]+a[3]+a[4])
print(sum(a))
print(a[4])
print(a[2:])
print(a[-5:-1])
a[0] = 98
print(a)
l1 = [1, 8, 7, 2, 21, 15]
print(l1) #unsorted
l1.sort()
print(l1) #sorted
l1.reverse()
print(l1)
l1.append(45) #adds at the end of the list
print(l1)
l1.insert(3,500)
print(l1)
l1.sort()
print(l1)
l1.pop(4)  # pop() works at the index of the list
print(l1)
# l1.remove(15)
# print(l1)

#taking 7 seven fruits as user input in a list
f1=input("Enter the fruit number 1 :")
f2=input("Enter the fruit number 2 :")
f3=input("Enter the fruit number 3 :")
f4=input("Enter the fruit number 4 :")
f5=input("Enter the fruit number 5 :")
f6=input("Enter the fruit number 6 :")
f7=input("Enter the fruit number 7 :")

myfruitlist=[f1,f2,f3,f4,f5,f6,f7]
print(myfruitlist)