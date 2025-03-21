# numbers = [4, 0, 2, 0, 1, 6, 0, 3]
# numbers.sort()
# print(numbers)

n=int(input("Enter the number of terms:"))
# Collecting user inputs in a list
numbers = []
for i in range(n):
    num = int(input("Enter the list elements: "))
    numbers.append(num)

sorted_numbers = sorted(numbers, key=lambda x: (x == 0, x))  # Sort by zero condition

print("Original List:", numbers)
print("Sorted List with Zeros at End:", sorted_numbers)

# reversing this list
reverse=sorted_numbers[::-1]
print("The Reversed list is ",reverse)


# output
# Enter the number of terms:6
# Enter the list elements: 1
# Enter the list elements: 0
# Enter the list elements: 5
# Enter the list elements: 0
# Enter the list elements: 8
# Enter the list elements: 9
# Original List: [1, 0, 5, 0, 8, 9]
# Sorted List with Zeros at End: [1, 5, 8, 9, 0, 0]
# The Reversed list is  [0, 0, 9, 8, 5, 1]