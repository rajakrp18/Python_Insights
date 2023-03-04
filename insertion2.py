l = [9, 5, 6, 2, 8]
print(l)
for i in range(1, len(l)):
    temp = l[i]
    j = i-1
    while j >= 0 and l[j] > temp:
        l[j+1] = l[j]
        j = j-1
    l[j+1] = temp
    print(l)
