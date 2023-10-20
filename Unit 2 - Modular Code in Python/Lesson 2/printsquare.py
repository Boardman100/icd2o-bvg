def charsq(char, height):
    i = height
    if isinstance(char, (str)) and len(char)==1:
        while i>0:
            print(char*height)
            i -= 1
    else:
        print("Invalid Input")

char = input("Enter your character: ")
side = int(input("Enter your sqaure's side length: "))
charsq(char, side)