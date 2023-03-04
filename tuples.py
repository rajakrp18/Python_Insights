t=(1,2,3,4,5,1,1) # tuples are immutable that cannot be changed
# t[0]=5 # TypeError: 'tuple' object does not support item assignment
print(t[2])
print(t)

t1=() #tuple with one element
print(t1)
t2=(1,) #tuple with one element
print(t2)

#methods in tuples 
print(t.count(1)) #giving us the number of occurence of 1
print(t.index(1)) #giving the index of 1 

