# list=[1,2,2,3,4,4,5,6]
# print(list)

# list user input
n = int(input("Enter number of elements: "))  # User specifies size
list = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))  # Input each element
    list.append(num)

print("User Input List:", list)

for i in range(len(list)):
    for j in range(i+1,len(list)-1):
        if list[i]==list[j]:
            # del list[j]
            list.pop(j)
print(list)

# reversing this list
reverse=list[::-1]
print(reverse)


# output
# Enter number of elements: 5
# Enter element 1: 1
# Enter element 2: 2
# Enter element 3: 2
# Enter element 4: 3
# Enter element 5: 4
# User Input List: [1, 2, 2, 3, 4]
# [1, 2, 3, 4]
# [4, 3, 2, 1]