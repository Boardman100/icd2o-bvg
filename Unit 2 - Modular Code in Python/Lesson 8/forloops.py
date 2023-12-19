#prints numbers 1-5
def example_one():
    for counter in range(1,6):
        print(counter)

#prints numbers 0-9, if no start point is put in it is assumed to begin at 0
def example_one_a():
    for counter in range(10):
        print(counter)

#Adds numbers from start to finish(counting end)
def example_two(start,finish):
    total = 0
    for i in range(start,finish+1):#+1 counts to endpoint
        total += i
    print(total)

#Prints numbers from 20-1 and goes down by steps of 2(steps must be integers)
def example_three():
    for i in range(20,0, -2):
        print(i)

#Prints a string backwards
#range(start index in string, end index in string, step), if step is not included it is assumed to be +1
def example_four(str):
    result = ""
    for i in range(len(str)-1,-1,-1):#Ends at -1 which means that it prints every character in string starting with 0, 
        result += str[i]
        print(result)

#Grabs substring of length n and prints them
def example_five(str,n):
    for i in range(0,len(str)-n+1):
        print(str[i:i+n])

#Counts how many times the second word appears in the first word
def example_six(str1,str2):
    if len(str2)>len(str1):
        return 0
    result = 0
    for i in range(0,len(str1)-len(str2)+1):
        if str1[i:len(str2)+i] == str2:
            result += 1
    print(result)
example_six("aywhyay","ay")