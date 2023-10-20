def chartri(char, height):
    i = 1
    if isinstance(char, (str)) and len(char)==1:
        for i in range(1,height+1):
            print(char*i)
            i += 1
    else:
        print("Invalid Input")

char = input("Enter your character: ")
height = int(input("Enter your height: "))
chartri(char, height)