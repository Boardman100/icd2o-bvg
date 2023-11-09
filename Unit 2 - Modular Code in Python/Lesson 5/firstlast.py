def theEnd(s,front):
    if front == True:
        char = s[0]
    else:
        length = len(s)
        char = s[length-1]
    return char
print(theEnd("hello",False))