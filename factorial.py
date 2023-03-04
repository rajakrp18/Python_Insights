# # n!=1*2*3*4*...*n
# n = 4
# product = 1
# for i in range(1, n+1):
#     '''for can be used to traverse a list'''
#     # print(i, n, product)
#     product = product*(i)
#     print(i, n, product)

# print(product)
# # print(product.__doc__)
# print(i, n, product)

# sum of natural numbers
# Sn = n(n+1)/2

# def nnatural(n=5):
#     return n*(n+1)/2


# sn = nnatural(9)
# print(f"The Sum of Natural Numbers given are {sn}")

# # function to convert degree celsius to fahrenheit
# # and also fahrenheit to degree celsius


# def fahrenheit(Celsius):
#     return ((Celsius * (9/5)) + 32)


# print(f"Given temperature is  : {24} in degree Celsius ")
# print(f"The converted Fahrenheit temperature is : {fahrenheit(24)}")


# def Celsius(fahrenheit):
#     return (fahrenheit - 32) * 5/9


# print(f"Given temperature is  : {75.2} in degree Fahrenheit ")
# print(f"The converted Celsius temperature is : {Celsius(75.2)}")

# to print simple star pattern using for loop
# n = int(input("Enter the desired number of rows :"))
# for i in range(0, n):
#     for j in range(0, n-i):
#         print("*", end="")
# print(" ")

# n = int(input("Enter the number of desired rows :"))
# for i in range(n):
#     print("*" * (n-i))

# write a function python to strip the blank spaces and also remove the first word of the sentence
this = "   Raj is a good boy   "
print(this)
print(this.strip())
