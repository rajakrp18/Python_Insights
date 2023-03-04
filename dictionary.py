myDict = {  # dictionaries are unordered and are mutable
    "Fast"  : "In a quick manner",
    "Raj"   : "a coder",
    "Marks" : [1, 2, 4],
    "anotherdict": {"raj": "pro gamer", "raj1": "good boy"},
    1 : 2  # we can also keep key value pair as integer-integer in a dictionary
}
print(myDict['Fast']) #this will print the values of the keys 
print(myDict['Raj'])
print(myDict['Marks'])
myDict['Marks'] = [80, 99, 100]  # updating / changing the values
print(myDict['Marks'])
print(myDict['anotherdict']['raj1'])

# dictionary methods
print(myDict.keys())  # prints the keys of the dictionary
print(myDict.values())  # print the values of the dictionary
# items returns a tuple which consists of key and value pair both it will be useful for iteration
print(myDict.items())
print(type(myDict.keys())) 
print(list(myDict.keys())) #by default type list
updateDict = {  # updating a dictionary, if the value is present then it can update the previous value with the new one
    "Lovish": "friend",
    "Divya" : "friends",
    "Shuvam": "friendss",
    "Raj"   : "friendsss",  # changing the existing value with the new value
    "raj1"  : "friendssss"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("raj1"))  # this will give none if not found whereas if found then it will return the key value to us
# print(myDict["harry"]) #this will give a traceback if not present in the dictionary
