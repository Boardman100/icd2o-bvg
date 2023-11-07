def middle3(word):
    length = len(word)
    gap = int((length-3)/2)
    return word[gap:length-gap]
print(middle3("intelligent"))