def swapchar(str):
    length = len(str)
    return str[0:length-2]+str[length-1:length]+str[length-2:length-1]
print(swapchar("words"))