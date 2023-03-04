# using for loop
n = int(input("Enter a number :"))
fact = 1
for i in range(1, n+1):
    fact = fact*i

print(f"The factorial of {n} is : {fact}")


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

# using function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)


f = fact(6)
print(f"The factorial of 6 is : {f}")

a = 20
b = 10
print("A is greater") if(a > b) else print(
    "=") if a == b else print("B is greater")


dict = {"street_name": "Hewlett Rd",
        "pin_code ": "743145",
        "city": "Kanchrapara",
        "dept": "MCA",
        "Marks_of_3_subjects": [84, 75, 90]}

for key, value in dict.items():
    print(key, value)

numbers = [1, 3, 4, 2]

# Sorting list of Integers
numbers.sort()
print(numbers)

txt = open("wel.txt", "w+")
txt.write("Welcome! Please have a seat")
txt.close()

txt = open("wel.txt", "r")
print(txt.read())
txt.close()
