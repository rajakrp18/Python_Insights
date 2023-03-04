# try:
#     a = g
#     b = 0
#     print(f"division result of {a}/{b}is {a/b}")

# except ZeroDivisionError as e:
#     print(e)
# except NameError as e:
#     print(e)

def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed")
    # print("I am always executed")


x = func1()
print(x)
