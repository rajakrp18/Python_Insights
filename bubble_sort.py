l = [10, 2, 12, 5, 17, 15]
print(l)
for i in range(0, len(l)):
    for j in range(0, len(l)-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            print(l)
