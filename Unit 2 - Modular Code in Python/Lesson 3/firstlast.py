def firstlast(str1,str2):
    length = len(str2)

    return str1[0:1]+str2[length-1:length]
print(firstlast("words","birds"))