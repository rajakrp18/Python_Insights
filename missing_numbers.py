# Taking user input
n = int(input("Enter the number of terms: "))

# Collecting user inputs in a list
numbers = []
for i in range(n):
    num = int(input("Enter the number: "))
    numbers.append(num)

print("Original List:", numbers)

# Sorting the list
numbers.sort()

# Generating the full range from min to max
filled_numbers = list(range(min(numbers), max(numbers) + 1))

# Finding the missing numbers
missing_numbers = sorted(set(filled_numbers) - set(numbers))

print("Complete List:", filled_numbers)
print("Missing Numbers:", missing_numbers)



# output
# Enter the number of terms: 5
# Enter the number: 1
# Enter the number: 5
# Enter the number: 7
# Enter the number: 9
# Enter the number: 15
# Original List: [1, 5, 7, 9, 15]
# Complete List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Missing Numbers: [2, 3, 4, 6, 8, 10, 11, 12, 13, 14]