dict = {"Name": "Raj Poddar", "Roll": "17", "ID": "100",
        "Dept": "MCA", "Marks of 5 subjects": [100, 90, 89, 75, 85]}
''''print(dict["Marks of 5 subjects"])
print(dict.keys())
print(dict.values())
print(sum(dict["Marks of 5 subjects"]))
print(dict["Marks of 5 subjects"][0]+dict["Marks of 5 subjects"][1] +
      dict["Marks of 5 subjects"][2]+dict["Marks of 5 subjects"][3]+dict["Marks of 5 subjects"][4])

for key in dict.keys():
    print(dict[key])
  '''  
sum = 0
for i in range(0,5):
    # print(dict["Marks of 5 subjects"][i])
    sum = sum + int(dict["Marks of 5 subjects"][i])
print(sum)
sum=0
for i in dict["Marks of 5 subjects"]:
    sum+=i
print(sum)