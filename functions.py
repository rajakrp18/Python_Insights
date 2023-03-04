# def calgmean(a, b):
#     mean = (a*b)/(a+b)
#     print("The geometric mean is :",mean)


# def isgreater(a, b):
#     '''this is a function which calculates which number is greater '''
#     if a > b:
#         print(f'In {a,b} the first number is greater')
#     else:
#         print(f'In {a,b} the second number is greater or equal to')


# def islesser():
#     '''we will write this function later-on'''
#     pass


# # a = 9
# # b = 18
# a = int(input("Enter the first number :"))
# b = int(input("Enter the second number :"))

# calgmean(a, b)
# isgreater(a, b)
# print(isgreater.__doc__)
# print(islesser.__doc__)

# # print(f'It will be floor number {usf} in US')
# # print("second number is greater or equal")
# # gmean1=(a*b)/(a+b)
# # print(gmean1)

# # c = 8
# # d = 7
# c = int(input("Enter the first number :"))
# d = int(input("Enter the second number :"))
# calgmean(c, d)
# isgreater(c, d)

# # gmean2=(c*d)/(c+d)
# # print(gmean2)

# def average(a=9, b=1):
#     '''this function shows the default arguments'''
#     print("The average is", (a+b)/2)


# print(average.__doc__)
# average()       # examples
# average(6, 8)   # of
# average(a=5)    # default
# average(b=10)   # arguments

# average(b=21, a=9)  # keyword arguments


# def average1(a, b, c=1):  # required arguments
#     print("The average of three numbers is :", (a+b+c)/3)


# average1(5, 6)
# average1(a=10, b=15)


# variable length arguments
# def average2(*numbers):
#     sum = 0
#     print("value of *numbers :", numbers)
#     for i in numbers:
#         print("value of i :", i)
#         sum = sum+i
#         print("value of sum :", sum)
#     print("The average of the given numbers is :", sum/len(numbers))


# average2(2, 14, 5, 6)

# return type

# def average3(*numbers):
#     sum = 0
#     print("value of *numbers :", numbers)
#     for i in numbers:
#         print("value of i :", i)
#         sum = sum+i
#         print("value of sum :", sum)
#     # print("The average of the given numbers is :", sum/len(numbers))
#     return sum/len(numbers)


# c = average3(2, 14, 5, 6)
# print("The value is average is returned via c :", c)


# list comprehension which means genarating a list on the fly
# list = [i for i in range(10)]
# print(list)
# list = [i*i for i in range(10) if i % 2 == 0]
# print(list)
# import this # this is zen of python

# factorial of a number
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(3) = 3*2*1
# factorial(2) = 2*1
# factorial(1) = 1
# factorial(0) = 1
# so if we want factorial of a number then,
# we have to apply factorial(n) = n*factorial(n-1)

import time


def factorial(n):
    '''calculate the factorial of a given number using recursion'''
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)


# factorial(7)
n = 7
# n=int(input("Enter a number :"))
# for n in range(n,0):
print(f"The factorial of the given number {n} is : ", factorial(7))
n = n-1
print(f"The factorial of the given number {n} is : ", factorial(6))
n = n-1
print(f"The factorial of the given number {n} is : ", factorial(5))
n = n-1
print(f"The factorial of the given number {n} is : ", factorial(4))
n = n-1
print(f"The factorial of the given number {n} is : ", factorial(3))
n = n-1
print(f"The factorial of the given number {n} is : ", factorial(2))
n = n-1
print(f"The factorial of the given number {n} is : ", factorial(1))
n = n-1
print(f"The factorial of the given number {n} is : ", factorial(0))


# def fahrenheit(Celsius):
#     return ((Celsius * (9/5)) + 32)


# print(f"Given temperature is  : {24} in degree Celsius ")
# print(f"The converted Fahrenheit temperature is : {fahrenheit(24)}")

seconds = time.time()
print("Seconds since epoch =", seconds)
time.asctime()

list = ['Raj', 'is', 'a', 'good', 'boy']

# for item in list:
#     print(item, "and", end=' ')
# we can simply replicate the following using the join () also

a = " and ".join(list)
print(a, end=' '"Other Boys are also good..!")

# beer song
word = "bottles"
for beer_num in range(2, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()

# vowels or not
vowels = ['a', 'e', 'i', 'o', 'u']
word = "Millet"
for letters in word:
    if letters in vowels:
        print(letters, "Is a Vowel")
    else:
        print(letters, "Is Not a Vowel")

# extended vowel program
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the words to be searched :")
# word = 'Millet'
found = []
for letter in word:
    if letter in vowels:
        # print(letter)
        if letter not in found:
            found.append(letter)
for vowels in found:
    print(vowels)

# another form using dictionary and counter
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the words to be searched :")
found = {}

found['a'] = 0
found['i'] = 0
found['o'] = 0
found['e'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1
for k, v in sorted(found.items()):
    print(f"{k} was found {v} time(s).")

# another version using sets
vowels = set('aeiou')
words = input("Enter the word to be searched :")

found = vowels.intersection(set(words))
for vowels in found:
    print(vowels)
