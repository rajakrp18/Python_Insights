def print_pattern(n):
    """This pattern is capable of printing the pattern 1,0,22,23,43,65,64,107,85,149,106,191,127,233...upto n no of terms."""

    pattern=[1,0] #Initialzing the sequences with its first two elements 
    j=1 #j=1 for odd indices 
    var=0 #var is the variable in the odd indices increment

    for i in range(2,n):
        if i%2==0:
            next_sum=pattern[i-2]+21
        else:
            next_sum=23*j-var
            j=j+2
            var=var+4
        pattern.append(next_sum)

    print(', '.join(map(str,pattern))) #this statement is used for the comma placement


# print(print_pattern.__doc__)
n=14
print_pattern(n)