def squirrel_play(temp,is_summer):
    play = False
    if is_summer == True:
        if temp>=60 or temp<=100:
            play = True
    else:
        if temp>=60 or temp<=90:
            play = True
    return play
print(squirrel_play(70,True))