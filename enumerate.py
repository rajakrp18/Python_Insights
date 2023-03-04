
marks = [12, 10, 100, 99, 98, 10, 1]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 2):
#         print("Raj is awesome !")
#     index += 1
# same can be done using enumerate in a painfree process

# index = 0
for index, mark in enumerate(marks):
    print(index, mark)
    if(index == 1):
        print("Raj is awesome !")
    # index += 1
