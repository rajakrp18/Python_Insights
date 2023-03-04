def listuserinput():
    """This a function that takes the list elements as user input from the user and prints it"""
    lr = []
    for j in range(0, 5):
        i = int(input("Enter an element:"))
        lr.append(i)
    print(lr)


print(listuserinput.__doc__)
listuserinput()
