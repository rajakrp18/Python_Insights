# selection sorting means selecting the lowest value and placing it at the starting
x = [10, 2, 12, 5, 17, 15]
print(f"{x} <-- unsorted array ")

for i in range(0, len(x)-1):  # (n-1) iterations are required for the sorted array
    min = x[i]  # current minimum value stored in min
    print(f"{min} <--current minimum value")
    # print(f"{x} this part is within for i ")

    for j in range(i+1, len(x)):
        if x[i] > x[j]:
            min = x[j]  # overwriting the current min to present min value
            print(f"{min} <--present minimum value")
            # print(f"{x} this part is within for j(upper) ")
            x[i], x[j] = x[j], x[i]
            # print(f"{x} this part is within for j(lower)")
            # print(f"{x} <-- sorted array ")
print(f"{x} <-- sorted array ")
